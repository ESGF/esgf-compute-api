# ESGF Compute end-user API

> The ESGF Compute end-user API provides an object-oriented climatology package
to access large scale computational resources through the Web Processing
Service interface standard.

Supported WPS version: 1.0.0

### Installation

```
conda install -c conda-forge -c uvcdat esgf-compute-api
```

or

```
git clone https://github.com/ESGF/esgf-compute-api

cd esgf-compute-api

python setup.py install
```


### Quickstart

> [Getting Started](blob/master/examples/1_getting_started.ipynb)

or

```python
import cwt

tas = cwt.Variable('http://thredds/dap/test.nc', 'tas')

wps = cwt.WPSClient('http://localhost:8000/wps')

process = wps.get_process('CDAT.subset')

wps.execute(process, inputs=[tas], axes=['x', 'y'])

while process.processing:
  print process.status
```

### Docker image

Docker [image](blob/master/docs/source/cwt_docker.md) containing Jupyter notebook and ESGF CWT end-user api.

### Examples

Jupyter Notebook cotnaining examples can be found [here](tree/master/examples)

### Documentation

Documentation can be found on [here](tree/master/docs/source)

### Compatibility

Compatibility document can be found on [here](blob/master/docs/source/cwt.compat.rst)
