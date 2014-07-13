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


from distutils.core import setup

setup(name='vagrantappindicator',
      version='0.1',
      description='Vagrant Application Indicator for Ubuntu',
      url='.',
      author='.',
      author_email='.',
      package_dir = {'': 'src'},
      py_modules=['poc', 'machineindex'],
      package_data = {'': ['img/*.png']}
)
