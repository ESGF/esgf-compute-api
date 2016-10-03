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
.. testsetup:: *

    from mock import Mock
    from esgf import wps

    wps_mock = Mock()
    wps.WebProcessingService = wps_mock

    wps_inst = wps_mock.return_value
    wps_inst.processes = (Mock(identifier=x) for x in ['averager.mv'])

    from esgf import process

    process_mock = Mock()
    process_inst = process_mock.return_value
    process_inst.output = '63a9ffd4-e073-44f7-8fc3-33f96715224a http://0.0.0.0:8080/thredds/dodsC/test/fe74bed8-3121-444c-a904-2a3abd592404.cdf tas [] application/x-cdf'

    process.Process.from_identifier = process_mock

.. doctest:: quickstart

    >>> from esgf import WPS
    
    >>> from esgf import Variable

    >>> tas = Variable('http://thredds/dap/test.nc', 'tas')

    >>> wps = WPS('http://localhost:8000/wps/')

    >>> process = wps.get_process('averager.mv')

    >>> process.execute(inputs=[tas]) # doctest: +SKIP

    >>> process.output
    '63a9ffd4-e073-44f7-8fc3-33f96715224a http://0.0.0.0:8080/thredds/dodsC/test/fe74bed8-3121-444c-a904-2a3abd592404.cdf tas [] application/x-cdf'
