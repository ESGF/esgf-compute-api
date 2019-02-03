#!/usr/bin/env python

from setuptools import setup

setup(
    name='esgf-compute-api',
    description='Compute Working Team End-User API',
    packages=['cwt', 'cwt.wps', 'cwt.wps.raw'],
    author='Jason Boutte',
    author_email='boutte3@llnl.gov',
    version='2.1.0',
    url='https://github.com/ESGF/esgf-compute-api',
)
