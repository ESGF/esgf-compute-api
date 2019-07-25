# ESGF Compute end-user API
> The ESGF Compute end-user API provides an object-oriented climatology package
to access large scale computational resources through the Web Processing
Service interface standard.

Supported WPS version: 1.0.0

### Installation
[Conda](https://docs.conda.io/en/latest/miniconda.html) is the preferred method of install.
```
conda install -c conda-forge -c cdat esgf-compute-api
```
or can be installed from source.
```
git clone https://github.com/ESGF/esgf-compute-api

cd esgf-compute-api

python setup.py install
```
### Quickstart

You can start with the [Getting Started](examples/getting_started.ipynb) which is a [Jupyter](https://jupyter.readthedocs.io/en/latest/install.html) notebook that can be ran in a [JupyterLab](https://jupyter.org/install.html) instance.

or you can jump right into running some code.

**NOTE**: Some WPS services may require a token to access their compute resources.

```python
import cwt

tas = cwt.Variable('http://thredds/dap/test.nc', 'tas')

wps = cwt.WPSClient('http://localhost:8000/wps')

process = wps.process_by_name('CDAT.subset')

wps.execute(process, inputs=[tas])

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
