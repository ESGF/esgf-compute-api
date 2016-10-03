#########################
ESGF Compute end-user API
#########################

The ESGF Compute end-user API provides an object-oriented climatology package 
to access large scale computational resources through the Web Processing 
Service interface standard. The package is written on top of 
`OWSLib <https://github.com/geopython/OWSLib>`_ which supports 1.0.0 of the 
`WPS interface standard <http://www.opengeospatial.org/standards/wps>`_.

Installation
============
::

    python setup.py install

Quickstart
==========
::

    >>> from esgf import WPS
    
    >>> from esgf import Variable

    >>> tas = Variable('http://thredds/dap/test.nc', 'tas')

    >>> wps = WPS('http://localhost:8000/wps/')

    >>> process = wps.get_process('averager.mv')

    >>> process.execute(inputs=[tas], parameters=[NamedParameter('axes', 'longitude')]) # doctest: +SKIP

    >>> process.output
    '63a9ffd4-e073-44f7-8fc3-33f96715224a http://0.0.0.0:8080/thredds/dodsC/test/fe74bed8-3121-444c-a904-2a3abd592404.cdf tas [] application/x-cdf'

Documentation
=============

The simplest way to get the documentation currently is by building it.
The only requirement is sphinx being installed.

::

    pip install sphinx

    git clone https://github.com/ESGF/esgf-compute-api

    cd esgf-compute-api/docs

    make html

    open build/html/index.html
