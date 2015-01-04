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
import mock

from vgapplet import ui
from vgapplet import indicator
from vgapplet import machineindex

from . import samples


class TestAppIndicator(unittest.TestCase):
    def test_icon_choice(self):
        stopped = machineindex.Machine(None, "stopped", None, None)
        running = machineindex.Machine(None, "running", None, None)
        self.assertEquals("icon-0", indicator.VagrantAppIndicator._icon_name([stopped]*3))
        self.assertEquals("icon-1", indicator.VagrantAppIndicator._icon_name([running]*1))
        self.assertEquals("icon-2", indicator.VagrantAppIndicator._icon_name([running]*2))
        self.assertEquals("icon-3", indicator.VagrantAppIndicator._icon_name([running]*3))
        self.assertEquals("icon-3", indicator.VagrantAppIndicator._icon_name([running]*4))


if __name__ == "__main__":
    unittest.main()
