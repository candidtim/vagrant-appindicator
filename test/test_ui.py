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

import unittest
from unittest import mock

import vagrantindicator
import machineindex

import samples


class TestUi(unittest.TestCase):
    def test_notifications(self):
        with samples.SampleIndex() as sample_index, samples.SampleGtkEnvironment() as gtk_env:
            indicator = vagrantindicator.VagrantAppIndicator()
            indicator._show_notification = mock.Mock()
            machineindex.get_machineindex = mock.Mock(return_value=[])
            sample_index.touch()
            gtk_env.wait_for(lambda: indicator._show_notification.called)
            self.assertEqual(indicator._show_notification.call_count, 1)
            indicator._shutdown()


if __name__ == "__main__":
    unittest.main()
