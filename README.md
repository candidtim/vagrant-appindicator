# Vagrant Application Indicator for Ubuntu

Application Indicator to display *last known* state of Vagrant-managed VMs in the
notification area (system tray) on Ubuntu Unity and in Gnome.

Main features:

- displays last known state of VMs
- allows opening Terminal in the VM home directory from the indicator menu
- allows bringing VMs up, halting them and destroying them via an indicator menu


# Usage

To run Vagrant AppIndicator:

1. Clone the repository
2. `cd vagrant-appindicator`
3. `nohup make run &`

If you think there might be a better way to run it, I'm with you. I'm not
even sure if this can count as a *way to run* it, but is the only way currently.
Ideally, I would like to distribute it as a Debian package via the PPA, 
install a .desktop file for it to be discoverable in Unity's application 
search, and start it on user log in. All this is planned, and related pull 
requests are more than welcome.


# Development

## Project directory layout

- `./img/` - image files used in runtime (icons)
- `./src/` - appindicator source code (runtime)
- `./test/` - appindicator tests
- `Makefile` - provides basic tasks to run tests, run appindicator, etc.
- `setup.py` - python packaging script

## Running tests

    $ make venv  # run only once, or run again to re-create the virtualenv
    $ make tests

## Getting test coverage (reports to ./coverage/)

	$ make cover

## Creating python source package

    $ make sdist

## Running appindicator without installing it

    $ make run

## Cleaning up the project directory (remove dist/, \*.pyc, etc.)

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

## Documentation

1. Document (better) how to run
2. Document (better) how to develop 
3. Create sample screenshot and add to the documentation

## Refactorings

It is always good to clean up some code. Other than that:

1. Test somehow (how?) Gtk code (main module, menus, etc.) 
