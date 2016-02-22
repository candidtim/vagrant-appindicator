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

import json
import pkg_resources

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen


def is_update_available():
    current_version = _current_version()
    latest_version = _latest_version()
    return current_version is not None \
        and latest_version is not None \
        and current_version != latest_version


def _current_version():
    try:
        version = u'v%s' % pkg_resources.get_distribution("vagrantappindicator").version
    except pkg_resources.DistributionNotFound:
        version = None
    return version


def _latest_version():
    try:
      response = urlopen('https://api.github.com/repos/candidtim/vagrant-appindicator/tags')
      raw_json = response.read().decode('ascii')
      tags = json.loads(raw_json)
      latest_version = [tag['name'] for tag in tags][0]
    except:
      latest_version = None
    return latest_version
