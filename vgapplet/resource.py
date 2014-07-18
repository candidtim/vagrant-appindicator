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


import sys
from os.path import join, dirname, isfile


RESOURCES_DIRECTORY_PATH = "/usr/share/vgapplet"

# when running vgapplet directly from sources - use reosurces from sources as well
__RELATIVE_RESOURCE_PATH = join(dirname(dirname(__file__)))
__CURRENT_RESOURCES_PATH = \
	__RELATIVE_RESOURCE_PATH \
	if isfile(join(__RELATIVE_RESOURCE_PATH, "bin", "vgapplet")) else \
	RESOURCES_DIRECTORY_PATH


def image_path(name):
    """Returns path to the image file by its name"""    
    return join(__CURRENT_RESOURCES_PATH, "img", "%s.svg" % name)
