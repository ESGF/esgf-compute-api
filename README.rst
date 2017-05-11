#########################
ESGF Compute end-user API
#########################

The ESGF Compute end-user API provides an object-oriented climatology package 
to access large scale computational resources through the Web Processing 
Service interface standard.

Supported WPS version: 1.0.0

Installation
============
:: 
    
    conda install -c conda-forge -c jasonb857 esgf-compute-api

or

::

    git clone https://github.com/ESGF/esgf-compute-api

    cd esgf-compute-api

    python setup.py install


Quickstart
==========
::

    >>> import cwt

    >>> tas = cwt.Variable('http://thredds/dap/test.nc', 'tas')

    >>> wps = cwt.WPS('http://localhost:8000/wps')

    >>> process = wps.get_process('CDAT.subset')

    >>> wps.execute(process, inputs=[tas], axes=['x', 'y'])

    >>> while process.processing:
    
    >>>         print process.status

Examples
========

Jupyter Notebook examples can be found `here <https://github.com/ESGF/esgf-compute-api/tree/master/examples>`_

Documentation
=============

Documentation can be found on `readthedocs <http://esgf-compute-api.readthedocs.io/en/latest>`_

Compatibility
=============

:doc:`cwt.compat`
