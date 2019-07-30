#!/usr/bin/env python

import os
import re
from setuptools import setup

install_path = os.path.dirname(__file__)

ver_path = os.path.join(install_path, 'cwt', '_version.py')

with open(ver_path) as infile:
    data = infile.readline()

__version__ = re.search('((\\d\\.?)+)', data).group(0)

setup(
    name='esgf-compute-api',
    description='Compute Working Team End-User API',
    packages=['cwt'],
    author='Jason Boutte',
    author_email='boutte3@llnl.gov',
    version=__version__,
    url='https://github.com/ESGF/esgf-compute-api',
    install_requires=[
        "owslib>=0.17.1",
    ],
    tests_require=[
        "pytest>=5.0.1",
        "mock>=3.0.5",
    ]
)
