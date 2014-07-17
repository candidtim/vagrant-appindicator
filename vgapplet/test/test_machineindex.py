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


import io
import unittest

from vgapplet import machineindex

from . import samples


class TestMachineIndex(unittest.TestCase):
    def test_parser(self):
        sample_string_io = io.StringIO(samples.MACHINEINDEX_SAMPLE)
        machines = machineindex._parse_machineindex(sample_string_io)
        self.assertEqual(len(machines), 1)
        machine = machines[0]
        self.assertEqual(machine.id, samples.SAMPLE_MACHINE_ID)
        self.assertEqual(machine.state, samples.SAMPLE_MACHINE_STATE)
        self.assertEqual(machine.directory, samples.SAMPLE_MACHINE_DIRECTORY)
        self.assertEqual(machine.name, samples.SAMPLE_MACHINE_NAME)


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
        with samples.SampleIndex():
            machineindex_path = machineindex._resolve_machineindex_path()
            self.assertEqual(machineindex_path, samples.SAMPLE_INDEX_FILE)


    def test_resolve_machineindex_failure(self):
        self.assertRaises(Exception, machineindex._resolve_machineindex_path)


    def test_get_machineindex(self):
        with samples.SampleIndex():
            machines = machineindex.get_machineindex()
            self.assertEqual(len(machines), 1)


    def test_subscribe(self):
        new_machines = None
        def change_listener(machines):
            nonlocal new_machines
            new_machines = machines

        with samples.SampleIndex() as sample_index, samples.SampleGtkEnvironment() as gtk_env:
            machineindex.subscribe(change_listener)
            sample_index.touch()
            gtk_env.wait_for(lambda: new_machines is not None)
            self.assertIsNotNone(new_machines)
            self.assertEqual(new_machines[0].id, samples.SAMPLE_MACHINE_ID)
            machineindex.unsubscribe_all()


if __name__ == "__main__":
    unittest.main()
