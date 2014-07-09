# Vagrant Application Indicator for Ubuntu

## Project directory layout

./img/ - image files used in runtime (icons)
./src/ - appindicator source code (runtime)
./test/ - appindicator tests (only ran manually)
Makefile - provides basic tasks to run tests, create distribution, run appindicator, etc.
setup.py - packaging script

## Running tests

    $ make venv  # run only once, or run again to re-create the virtualenv
    $ make tests

## Getting test coverage (reports to ./coverage/)

	$ make cover

## Packaging

    $ make sdist

## Running appindicator without installing it

    $ make run

## Cleaning up the project directory (remove dist/, *.pyc, etc.)

    $ make clean
