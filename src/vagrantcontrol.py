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
