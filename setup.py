#!/usr/bin/env python

import cwt
from distutils.core import setup

setup(name='esgf-compute-api',
      version=cwt.__version__,
      description='Compute Working Team End-User API',
      author='Jason Boutte',
      author_email='boutte3@llnl.gov',
      url='https://github.com/ESGF/esgf-compute-api',
      packages=['cwt', 'cwt.wps_lib'],
)
