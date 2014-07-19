# Vagrant Application Indicator for Ubuntu

Application Indicator to display *last known* state of Vagrant-managed VMs in the
notification area (system tray) on Ubuntu Unity and in Gnome.

Main features:

- displays last known state of VMs
- shows notifications when machines state changes
- allows opening Terminal in the VM home directory from the indicator menu
- allows bringing VMs up, halting them and destroying them via an indicator menu


# Usage

**Install**:

    $ sudo pip install git+https://github.com/candidtim/vagrant-appindicator.git

**Run**

To run Vagrant AppIndicator, start it from Unity Dash or Gnome Desktop Menu (whichever
desktop you use).

**Few more details, if you want**

Install process will install the indicator directly from the source code on GitHub. 
`pip` basically clones the repo and builds and installs everything locally. One can as
well do all that manually (why though?) - see below if you're interested.

Just in case, you can as well run Vagrant AppIndicator from command line: use `vgapplet` 
or, `nohup vgapplet &`.

To uninstall Vagrant AppIndicator and all files accompanying it, run 
`sudo pip uninstall vagrantappindicator`.


# Development

## Project directory layout

- `bin/` - entry point scripts
- `img/` - image files used in runtime (icons)
- `vgapplet/` - root application package (all source code)
- `**/test/` - test packages
- `Makefile` - provides basic tasks to run tests, run appindicator, etc.
- `setup.py` - python packaging script
- `README` - readme file for distributed pacakge
- `README.md` - this file

## Python 2 and Python 3

Current indicator implementation runs on both Python 2.7 and Python 3. All 
tests are as well executed on "both pythons".

## Running and testing

**Running tests**

    $ make venv  # run only once, or run again to re-create the virtualenv
    $ make tests

**Getting test coverage (reports to ./coverage/)**

    $ make cover

**Creating python source package**

    $ make sdist

**Running appindicator without installing it**

    $ make run

**Building and installing/uninstalling locally**

    $ sudo make install
    $ sudo make uninstall

**Cleaning up the project directory (remove dist/, \*.pyc, etc.)**

    $ make clean


# Roadmap

Further possible improvements are in several possible directions, as below.
Pull requests are very welcome.

## Installation and Distribution

1. Create minimalistic distribution (downloadable python package?)
2. Ultimately, distribute via PPA

## Features

1. Extend to support Docker (and probably VirtualBox?)
2. Handle more statuses (not only poweroff and running, but also other transit and error statuses)
3. Get better icons for states (indicate state with colors?)

## Documentation

1. Document (better) how to run
2. Document (better) how to develop 
3. Create sample screenshot and add to the documentation

## Refactorings

It is always good to clean up some code. Other than that:

1. Test (better) UI code
2. Replace Gio file monitoring with non-Gtk-based techniques?


# Copying

Copyright 2014, [candidtim](https://github.com/candidtim)

This Application Indicator is distributed under 
[GNU GENERAL PUBLIC LICENSE](http://www.gnu.org/licenses/gpl.html), 
either version 3 of the License, or (at your option) any later version.

![GPLv3](http://www.gnu.org/graphics/gplv3-88x31.png)

This copyright or licensing doesn't apply to the icons used in the AppIndicator.
See Attributions below.

# Attributions

Icons used in this AppIndicator were originally distributed under 
[CC BY 3.0 license](http://creativecommons.org/licenses/by/3.0/). Neither
of the resorces listed below were modified, and they were used as is.

- Main AppIndicator icon: icon made by Picol from [www.flaticon.com](http://www.flaticon.com)
- Play/Stop icons: icons made by [Freepik](http://www.freepik.com) from [www.flaticon.com](http://www.flaticon.com/free-icon/play-button-arrowhead_27223)
