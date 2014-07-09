#!/usr/bin/python

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
