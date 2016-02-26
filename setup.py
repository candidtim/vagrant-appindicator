#!/usr/bin/python3

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
from distutils.core import setup

from vgapplet.resource import RESOURCES_DIRECTORY_PATH


def find_resources(resource_dir):
    target_path = os.path.join(RESOURCES_DIRECTORY_PATH, resource_dir)
    resource_names = os.listdir(resource_dir)
    resource_list = [os.path.join(resource_dir, file_name) for file_name in resource_names]
    return (target_path, resource_list)


setup(name="vagrantappindicator",
      version="1.4.0",
      description="Vagrant Application Indicator for Ubuntu",
      url='https://github.com/candidtim/vagrant-appindicator',
      author='candidtim',
      author_email='timcandid@gmail.com',
      license='GPL',
      packages=["vgapplet"],
      data_files=[
          ('/usr/share/applications', ['vgapplet.desktop']),
          find_resources("img/light"),
          find_resources("img/dark")],
      scripts=["bin/vgapplet"]
)
