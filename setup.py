#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = 'esgf-compute-api',
    version = '1.0',
    packages = find_packages('esgf'),
    install_requires = [
        'OWSLib>=0.11.2',
    ],
)
