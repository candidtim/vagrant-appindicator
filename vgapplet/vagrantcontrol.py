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
import pwd
import getpass
import subprocess


def open_terminal(machine):
    """Simply opens new terminal window in the working directory of a given machine"""
    subprocess.Popen(["x-terminal-emulator"], cwd=machine.directory)


def start(machine):
    __term("vagrant up %s" % machine.name, machine.directory)


def start_and_provision(machine):
    __term("vagrant up --provision %s" % machine.name, machine.directory)


def resume(machine):
    __term("vagrant resume %s" % machine.name, machine.directory)


def suspend(machine):
    __term("vagrant suspend %s" % machine.name, machine.directory)


def ssh(machine):
    __term("vagrant ssh %s" % machine.name, machine.directory)


def halt(machine):
    __term("vagrant halt %s" % machine.name, machine.directory)


def provision(machine):
    __term("vagrant provision %s" % machine.name, machine.directory)


def destroy(machine):
    __term("vagrant destroy --force %s" % machine.name, machine.directory)


def __term(command, cwd):
    """Starts new terminal, executes given command in it and falls back to user's default shell after its completion"""
    subprocess.Popen(['x-terminal-emulator', '-e', 'bash -c "%s; exec %s"' % (command, __user_shell())],
                     cwd=os.path.abspath(cwd))

def __user_shell():
    return pwd.getpwnam(getpass.getuser()).pw_shell
