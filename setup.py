#!/usr/bin/env python

from setuptools import setup
from setuptools.command.test import test as TestCommand

import esgf

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)

        self.test_args = []

    def run_tests(self):
        import sys
        import pytest

        errcode = pytest.main(self.test_args)

        sys.exit(errcode)

setup(
    name='esgf-compute-api',
    version=esgf.__version__,
    url='http://github.com/ESGF/esgf-compute-api',
    author='Jason Boutte',
    test_require=['pytest'],
    install_requires=['requests'],
    cmdclass={'test': PyTest},
    author_email='boutte3@llnl.gov',
    description='ESGF CWT End-user API',
    packages=['esgf']
)
