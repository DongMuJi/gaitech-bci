#!/usr/bin/env python
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup()
d['packages'] = ['gaitech_bci_teleop', 'gaitech_bci_teleop.interface']
d['package_dir'] = {'':'src'}

setup(**d)
