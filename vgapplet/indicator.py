#!/usr/bin/python3

# Copyright 2014, candidtim (https://github.com/candidtim)
#
# This file is part of Vagrant AppIndicator for Ubuntu.
#
# Vagrant AppIndicator for Ubuntu is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Foobar is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with Foobar.
# If not, see <http://www.gnu.org/licenses/>.

import sys
import os
import signal

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify

from . import config
from . import ui
from . import resource
from . import machineindex
from . import vagrantcontrol


APPINDICATOR_ID = 'vagrant_appindicator'


class VagrantAppIndicator(object):
    def __init__(self):
        notify.init(APPINDICATOR_ID)
        self.indicator = appindicator.Indicator.new(
            APPINDICATOR_ID, resource.image_path("icon", ui.THEME), appindicator.IndicatorCategory.SYSTEM_SERVICES)
        self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
        self.last_known_machines = None

        # trigger first update manually, and then subscribe to real updates
        try:
            self.update(machineindex.get_machineindex())
            machineindex.subscribe(self.update)
        except machineindex.MachineIndexNotFoundError:
            notify.Notification.new(
                "<b>Is Vagrant installed?</b>",
                "Either Vagrant is not installed, or never ran, or its version is too old (has no public machine index)",
                None).show()
            sys.exit(1)


    def _shutdown(self):
        machineindex.unsubscribe_all()


    def run(self):
        gtk.main()


    def open_about_page(self):
        import webbrowser
        webbrowser.open('https://github.com/candidtim/vagrant-appindicator/#vagrant-application-indicator-for-ubuntu-unity--gnome')


    def quit(self):
        self._shutdown()
        notify.uninit()
        gtk.main_quit()


    def update(self, machines):
        """Entry point for appindicator update.
        Triggers all UI modifications necessary on updates of machines states
        Subscribed as a listener to updates of machineindex"""
        self.__update_icon(machines)
        self.__notify_about_changes(machines)
        self.__update_menu(machines)
        self.last_known_machines = machines


    def __update_icon(self, machines):
        """Updates main appindicator icon to reflect the number of running machines
        Icons indicate if no, 1, 2 or 3 machines are running; more running machines
        are shown same way as 3 running machines"""
        icon_name = VagrantAppIndicator._icon_name(machines)
        icon = resource.image_path(icon_name, ui.THEME)
        self.indicator.set_icon(icon)


    @staticmethod
    def _icon_name(machines):
        """Returns correct icon name, based on the number of running machines. See __update_icon()"""
        running_count = len([m for m in machines if m.isRunning()])
        icon_index = min(running_count, 3)
        return "icon-%d" % icon_index


    def _show_notification(self, title, message):
        """Shows balloon notification with given title and message"""
        if config.show_notifications:
            notify.Notification.new("<b>Vagrant - %s</b>" % title, message, None).show()


    def __notify_machine_state_change(self, title, machine):
        self._show_notification(title, "%s (%s)" % (machine.directory, machine.name))


    def __notify_about_changes(self, new_machines):
        """Shows balloon notifications for every change in machines states"""
        if not self.last_known_machines: return # only possible on first update

        diff = machineindex.diff_machineindexes(new_machines, self.last_known_machines)
        for new_machine in diff[0]:
            self.__notify_machine_state_change("New machine went %s" % new_machine.state, new_machine)
        for removed_machine in diff[1]:
            self.__notify_machine_state_change("Machine destroyed", removed_machine)
        for changed_machine in diff[2]:
            self.__notify_machine_state_change("Machine went %s" % changed_machine.state, changed_machine)


    def __update_menu(self, machines):
        """Updates appindicator menu with current machines state"""
        menu = gtk.Menu()

        for machine in machines:
            item = self.__create_machine_submenu(machine)
            menu.append(item)
        if not machines:
            menu.append(gtk.MenuItem("No active machines found (all machines destroyed?)"))

        menu.append(gtk.SeparatorMenuItem("Options"))

        item_show_notifications = \
            gtk.CheckMenuItem("Show notifications", active = config.show_notifications)
        item_show_notifications.connect("activate", self.on_show_notifications)
        menu.append(item_show_notifications)

        item_about = gtk.MenuItem('Help & About')
        item_about.connect('activate', self.on_about)
        menu.append(item_about)

        item_quit = gtk.MenuItem('Quit')
        item_quit.connect('activate', self.on_quit)
        menu.append(item_quit)

        menu.show_all()
        self.indicator.set_menu(menu)


    def __create_machine_submenu(self, machine):
        """Creates menu item for a given VM, with its submenu and relevant actions in it"""
        menu_item = gtk.ImageMenuItem("%s (%s) - %s" % (machine.directory, machine.name, machine.state))
        menu_item_image = gtk.Image()
        image_file_path = resource.image_path(machine.state, ui.THEME)
        if not os.path.isfile(image_file_path):
            image_file_path = resource.image_path("unknown", ui.THEME)
        menu_item_image.set_from_file(image_file_path)
        menu_item.set_image(menu_item_image)
        menu_item.set_always_show_image(True)
        
        submenu = gtk.Menu()
        menu_item.set_submenu(submenu)

        submenu_item_terminal = gtk.MenuItem('Open terminal...')
        submenu_item_terminal.connect('activate', self.on_open_terminal, machine)
        submenu.append(submenu_item_terminal)

        if machine.isPoweroff():
            submenu_item_up = gtk.MenuItem('Up')
            submenu_item_up.connect('activate', self.on_start_vm, machine)
            submenu.append(submenu_item_up)
        
        if machine.isRunning():
            submenu_item_halt = gtk.MenuItem('Halt')
            submenu_item_halt.connect('activate', self.on_halt_vm, machine)
            submenu.append(submenu_item_halt)

        submenu_item_destroy = gtk.MenuItem('Destroy')
        submenu_item_destroy.connect('activate', self.on_destroy_vm, machine)
        submenu.append(submenu_item_destroy)

        return menu_item

    # UI listeners
    def on_about(self, _): self.open_about_page()
    def on_quit(self, _): self.quit()
    def on_open_terminal(self, _, machine): vagrantcontrol.open_terminal(machine)
    def on_start_vm(self, _, machine): vagrantcontrol.start(machine)
    def on_halt_vm(self, _, machine): vagrantcontrol.halt(machine)
    def on_destroy_vm(self, _, machine): vagrantcontrol.destroy(machine)
    def on_show_notifications(self, _):
        config.show_notifications = not config.show_notifications
        config.persist()


def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    VagrantAppIndicator().run()


if __name__ == "__main__":
    main()
