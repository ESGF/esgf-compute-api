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

    from esgf import WPS
    from esgf import Variable

    tas = Variable('http://thredds/dap/test.nc', 'tas')

    wps = WPS('http://0.0.0.0:8000/wps/')
    
    process = wps.get_process('averager.mv')

    process.execute(variable=tas)

    process.output.download('./test.nc')
