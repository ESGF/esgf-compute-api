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

```
docker pull jasonb87/compute-api:2.2.0
```

##### Jupyter Lab

```
docker run -it -p 8888:8888 jasonb87/compute-api:2.2.0
```

Open a browser to http://0.0.0.0:8888/lab and the password will be "esgf".

#### IPython
```
docker run -it jasonb87/compute-api:2.2.0 ipython
```

### Examples

Jupyter Notebook cotnaining examples can be found [here](examples/)

### Compatibility

Compatibility document can be found on [here](docs/source/cwt.compat.rst)
