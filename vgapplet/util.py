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
import sys

from pkg_resources import Requirement, resource_filename


IMG_DIR_PATH = os.path.join(os.path.dirname(__file__), "..", "img")
IS_IN_PACKAGE = os.path.isdir(IMG_DIR_PATH)


def image_path(name):
    """Returns path to the image file by its name"""
    if IS_IN_PACKAGE:
    	return os.path.join(IMG_DIR_PATH, "%s.svg" % name)
    else:
    	return resource_filename(Requirement.parse("vagrantappindicator"), "img/%s.svg" % name)
