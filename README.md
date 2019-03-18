# ESGF Compute end-user API

> The ESGF Compute end-user API provides an object-oriented climatology package
to access large scale computational resources through the Web Processing
Service interface standard.

Supported WPS version: 1.0.0

### Installation

```
conda install -c conda-forge -c cdat esgf-compute-api
```

or

```
git clone https://github.com/ESGF/esgf-compute-api

cd esgf-compute-api

python setup.py install
```


### Quickstart

> [Getting Started](examples/getting_started.ipynb)

or

```python
import cwt

tas = cwt.Variable('http://thredds/dap/test.nc', 'tas')

wps = cwt.WPSClient('http://localhost:8000/wps')

process = wps.get_process('CDAT.subset')

wps.execute(process, inputs=[tas], axes='xy')

process.wait()
```

### Docker image

Docker [image](docs/source/cwt_docker.md) containing Jupyter lab and ESGF CWT end-user api.

### Examples

Jupyter Notebook cotnaining examples can be found [here](examples/)

### Compatibility

Compatibility document can be found on [here](docs/source/cwt.compat.rst)

