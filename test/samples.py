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
import time
import threading

from gi.repository import Gtk as gtk


MACHINEINDEX_SAMPLE = """
{
   "version":1,
   "machines":{
      "abcdef1234567890":{
         "local_data_path":"/home/user/vagrant/vm1/.vagrant",
         "name":"default",
         "provider":"virtualbox",
         "state":"running",
         "vagrantfile_name":null,
         "vagrantfile_path":"/home/user/vagrant/vm1",
         "updated_at":null,
         "extra_data":{
            "box":{
               "name":"hashicorp/precise64",
               "provider":"virtualbox",
               "version":"1.1.0"
            }
         }
      }
   }
}
"""

SAMPLE_MACHINE_ID = "abcdef1234567890"
SAMPLE_MACHINE_STATE = "running"
SAMPLE_MACHINE_DIRECTORY = "/home/user/vagrant/vm1"
SAMPLE_MACHINE_NAME = "default"

SAMPLE_INDEX_DIR = "/tmp/.vagrant.d/data/machine-index"
SAMPLE_INDEX_FILE = SAMPLE_INDEX_DIR + "/index"

_TEST_WAIT_TIMEOUT = 10 # seconds


class SampleIndex(object):
    def __enter__(self):
        os.makedirs(SAMPLE_INDEX_DIR)
        with open(SAMPLE_INDEX_FILE, 'w') as sample_index:
            sample_index.write(MACHINEINDEX_SAMPLE)
        return self

    def touch(self):
        with open(SAMPLE_INDEX_FILE, 'a') as sample_index:
            sample_index.write("")

    def __exit__(self, type, value, traceback):
        os.remove(SAMPLE_INDEX_FILE)
        os.removedirs(SAMPLE_INDEX_DIR)


class SampleGtkEnvironment(object):
    '''Provides active Gtk environment to run tests in'''
    def __enter__(self):
        return self

    def wait_for(self, predicate):
        '''Runs Gtk main loop until the predicate function returns true'''
        start = time.time()
        while not predicate() and time.time() - start < _TEST_WAIT_TIMEOUT:
            gtk.main_iteration_do(blocking=False)
        if time.time() - start >= _TEST_WAIT_TIMEOUT:
            raise AssertionError("Timeout reached while waiting for predicate to become True")

    def __exit__(self, type, value, traceback):
        pass
