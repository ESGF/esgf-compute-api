#!/usr/bin/env python

from setuptools import setup

required = [
    'owslib',
]

setup(
    name = 'esgf-compute-api',
    version = '1.0.0',
    packages = ['esgf'],
    install_requires = required,
    author = 'Jason Boutte',
    author_email = 'boutte3@llnl.gov',
    description = 'ESGF Compute end-user API',
    url = 'http://github.com/ESGF/esgf-compute-api',
)
