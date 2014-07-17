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


import os
import subprocess


def open_terminal(machine):
    """Simple opens new terminal window in the working directory of a given machine"""
    subprocess.Popen(["gnome-terminal"], cwd=machine.directory)


def start(machine):
    __term("vagrant up %s" % machine.name, machine.directory)


def halt(machine):
    __term("vagrant halt %s" % machine.name, machine.directory)


def destroy(machine):
    __term("vagrant destroy --force %s" % machine.name, machine.directory)


def __term(command, cwd):
    """Starts new terminal, execute given command in it and fall back to bash after its completion"""
    os.system(
        "gnome-terminal --working-directory=%s -e \"bash -c '%s; exec bash'\"" % \
        (os.path.abspath(cwd), command))
