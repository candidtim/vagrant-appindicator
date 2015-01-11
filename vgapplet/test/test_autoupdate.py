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

from vgapplet import autoupdate


class TestAppIndicator(unittest.TestCase):
    def test_get_latest_version(self):
        # this test assumes that all versions are tagged with tags starting with V
        version = autoupdate._latest_version()
        self.assertTrue(type(u'') == type(version))
        self.assertTrue(version.startswith('v'))


if __name__ == "__main__":
    unittest.main()
