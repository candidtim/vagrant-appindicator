import os

import appindicator
import gtk
import pynotify

import util
import machineindex
import vagrantcontrol


APPINDICATOR_ID = 'vagrant_appindicator'


class VagrantAppIndicator(object):
    def __init__(self):
        self.indicator = appindicator.Indicator(
            APPINDICATOR_ID, util.image_path("icon"), appindicator.CATEGORY_APPLICATION_STATUS)
        self.indicator.set_status(appindicator.STATUS_ACTIVE)
        self.last_known_machines = None
        # trigger first update manually, and then subscribe to real updates
        self.update(machineindex.get_machineindex())
        machineindex.subscribe(self.update)


    def update(self, machines):
        """Entry point for appindicator update.
        Triggers all UI modifications necessary on updates of machines states
        Subscribed as a listener to updates of machineindex"""
        self.__notify_about_changes(machines)
        self.__update_menu(machines)
        self.last_known_machines = machines


    def shutdown(self):
        gtk.main_quit()


    def __show_notification(self, title, message):
        """Shows baloon notification with given title and message"""
        pynotify.Notification("<b>Vagrant - %s</b>" % title, message).show()


    def __notify_about_changes(self, new_machines):
        """Shows baloon notifications for every change in machines states"""
        if not self.last_known_machines: return # only possible on first update

        diff = machineindex.diff_machineindexes(new_machines, self.last_known_machines)

        for new_machine in diff[0]:
            self.__show_notification("New machine went %s" % new_machine.state, 
                "%s (%s)" % (new_machine.directory, new_machine.name))
        for removed_machine in diff[1]:
            self.__show_notification("Machine destroyed", 
                "%s (%s)" % (removed_machine.directory, removed_machine.name))
        for changed_machine in diff[2]:
            self.__show_notification("Machine went %s" % changed_machine.state,
                "%s (%s)" % (changed_machine.directory, changed_machine.name))


    def __update_menu(self, machines):
        """Updates appindicator menu with current machines state"""
        menu = gtk.Menu()

        for machine in machines:
            item = self.__create_machine_submenu(machine)
            menu.append(item)

        item_quit = gtk.MenuItem('Quit')
        item_quit.connect('activate', quit)
        menu.append(item_quit)

        menu.show_all()
        self.indicator.set_menu(menu)


    def __create_machine_submenu(self, machine):
        """Creates menu item for a given VM, with its submenu and relvant actions in it"""
        menu_item = gtk.ImageMenuItem("%s (%s) - %s" % (machine.directory, machine.name, machine.state))
        menu_item_image = gtk.Image()
        menu_item_image.set_from_file(util.image_path(machine.state)) # TODO: handle all states
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
    def on_open_terminal(self, _, machine): vagrantcontrol.open_terminal(machine)
    def on_start_vm(self, _, machine): vagrantcontrol.start(machine)
    def on_halt_vm(self, _, machine): vagrantcontrol.halt(machine)
    def on_destroy_vm(self, _, machine): vagrantcontrol.destroy(machine)


def main():
    pynotify.init(APPINDICATOR_ID)
    indicator = VagrantAppIndicator()
    gtk.main()


if __name__ == "__main__":
    main()
