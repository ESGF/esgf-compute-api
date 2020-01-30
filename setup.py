#!/usr/bin/env python

from setuptools import setup

setup(
    name='esgf-compute-api',
    description='Compute Working Team End-User API',
    packages=['cwt'],
    author='Jason Boutte',
    author_email='boutte3@llnl.gov',
    version="2.2.3",
    url='https://github.com/ESGF/esgf-compute-api',
    install_requires=[
        "owslib>=0.17.1",
    ],
    tests_require=[
        "pytest>=5.0.1",
        "mock>=3.0.5",
    ]
)
