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
    
    conda install -c uvcdat esgf-compute-api

or

::

    git clone https://github.com/ESGF/esgf-compute-api

    cd esgf-compute-api

    python setup.py install


Quickstart
==========
`Getting Started <https://github.com/ESGF/esgf-compute-api/blob/master/examples/1_getting_started.ipynb>`_

::

    >>> import cwt

    >>> tas = cwt.Variable('http://thredds/dap/test.nc', 'tas')

    >>> wps = cwt.WPS('http://localhost:8000/wps')

    >>> process = wps.get_process('CDAT.subset')

    >>> wps.execute(process, inputs=[tas], axes=['x', 'y'])

    >>> while process.processing:
    
    >>>         print process.status

Docker image
============

Docker image containing the `jupyter notebook and API <https://github.com/ESGF/esgf-compute-api/tree/master/docs/source/cwt_docker.md>`_

Examples
========

Jupyter Notebook examples can be found `here <https://github.com/ESGF/esgf-compute-api/tree/master/examples>`_

Documentation
=============

Documentation can be found on `readthedocs <http://esgf-compute-api.readthedocs.io/en/latest>`_

Compatibility
=============

Compatibility document can be found on `readthedocs <https://esgf-compute-api.readthedocs.io/en/latest/cwt.compat.html>`_
