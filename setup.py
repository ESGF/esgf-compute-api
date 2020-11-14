#!/usr/bin/env python

from setuptools import setup

setup(
    name='esgf-compute-api',
    description='Compute Working Team End-User API',
    packages=['cwt'],
    author='Jason Boutte',
    author_email='boutte3@llnl.gov',
    version="2.3.7",
    url='https://github.com/ESGF/esgf-compute-api',
    install_requires=[
        "owslib>=0.17.1",
    ],
    tests_require=[
        "pytest>=5.0.1",
        "mock>=3.0.5",
    ],
    entry_points={
        'console_scripts': [
            'cwt-convert-document=cwt.utilities:command_document_to_data_inputs',
            'cwt-convert-data-inputs=cwt.utilities:command_data_inputs_to_document',
            'cwt-convert=cwt.utilities:command_convert',
        ]
    },
)
