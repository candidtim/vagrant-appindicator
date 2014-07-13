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
import io
import unittest


import machineindex


MACHINEINDEX_SAMPLE = """{"version":1,"machines":{"abcdef1234567890":{"local_data_path":"/home/user/vagrant/vm1/.vagrant","name":"default","provider":"virtualbox","state":"running","vagrantfile_name":null,"vagrantfile_path":"/home/user/vagrant/vm1","updated_at":null,"extra_data":{"box":{"name":"hashicorp/precise64","provider":"virtualbox","version":"1.1.0"}}}}}"""

SAMPLE_INDEX_DIR = "/tmp/.vagrat.d/data/machine-index"
SAMPLE_INDEX_FILE = SAMPLE_INDEX_DIR + "/index"


class TestMachineIndex(unittest.TestCase):
    def test_parser(self):
        sample_string_io = io.StringIO(MACHINEINDEX_SAMPLE)
        machines = machineindex._parse_machineindex(sample_string_io)
        self.assertEqual(len(machines), 1)
        machine = machines[0]
        self.assertEqual(machine.id, "abcdef1234567890")
        self.assertEqual(machine.state, "running")
        self.assertEqual(machine.directory, "/home/user/vagrant/vm1")
        self.assertEqual(machine.name, "default")


    def test_diff(self):
        m1 = machineindex.Machine("1", "running", "/home/vm1", "default")
        m2 = machineindex.Machine("2", "running", "/home/vm2", "default")
        m2_changed = machineindex.Machine("2", "poweroff", "/home/vm2", "default")
        m3 = machineindex.Machine("3", "poweroff", "/home/vm3", "default")
        m4 = machineindex.Machine("4", "poweroff", "/home/vm4", "default")

        old_machineindex = [m2, m3, m4]
        new_machineindex = [m1, m2_changed, m3]

        diff = machineindex.diff_machineindexes(new_machineindex, old_machineindex)
        
        self.assertEqual(len(diff), 3)

        new_machines = diff[0]
        removed_machines = diff[1]
        changed_machines = diff[2]

        self.assertEqual(len(new_machines), 1)
        self.assertEqual(new_machines[0], m1)

        self.assertEqual(len(removed_machines), 1)
        self.assertEqual(removed_machines[0], m4)

        self.assertEqual(len(changed_machines), 1)
        self.assertEqual(changed_machines[0], m2_changed)
        self.assertEqual(changed_machines[0].state, m2_changed.state)


    def test_resolve_machineindex(self):        
        try:
            self._create_test_index()
            machineindex_path = machineindex._resolve_machineindex_path()
            self.assertEqual(machineindex_path, SAMPLE_INDEX_FILE)
        finally:
            self._remove_test_index()


    def test_resolve_machineindex_failure(self):
        self.assertRaises(Exception, machineindex._resolve_machineindex_path)


    def test_get_machineindex(self):
        try:
            self._create_test_index()
            machines = machineindex.get_machineindex()
            self.assertEqual(len(machines), 1)
        finally:
            self._remove_test_index()


    def test_subscribe(self):        
        def change_listener(): pass
        try:
            self._create_test_index()
            machineindex.subscribe(change_listener)
            # that is the extent of this test - cannot 
            # test the listener itself in any simple way 
            # as it requires running gtk main loop
        finally:
            self._remove_test_index()


    def _create_test_index(self):
        os.makedirs(SAMPLE_INDEX_DIR)
        with open(SAMPLE_INDEX_FILE, 'w') as sample_index:
            sample_index.write(MACHINEINDEX_SAMPLE)
    

    def _remove_test_index(self):
        os.remove(SAMPLE_INDEX_FILE)
        os.removedirs(SAMPLE_INDEX_DIR)


if __name__ == "__main__":
    unittest.main()
