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

    git clone https://github.com/ESGF/esgf-compute-api

    cd esgf-compute-api

    git checkout updates_for_EDAS

    python setup.py install


Quickstart
==========
`Getting Started <https://github.com/ESGF/esgf-compute-api/blob/EDAS_docs/examples/edas/1_getting_started.ipynb>`_

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

Jupyter Notebook examples can be found `here <https://github.com/ESGF/esgf-compute-api/tree/EDAS_docs/examples/edas>`_

