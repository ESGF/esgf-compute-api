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

or you can jump right into running some code. You can find instructions to retrieve a token [here](docs/source/token.md).

```python
import cwt

# Create a variable from an OpenDAP url and the name of the variable.
tas = cwt.Variable('http://thredds/dap/test.nc', 'tas')

# Initialize the client with the url to the WPS endpoint and the Token/API key.
wps = cwt.WPSClient('http://localhost:8000/wps', api_key='<TOKEN>')

# Select the process to execut.
process = wps.process_by_name('CDAT.subset')

# Execut the process.
wps.execute(process, inputs=[tas])

# Wait for the process to complete, this will print status message to the console.
process.wait()

# Prints the output of the process which is either an instance of cwt.Variable, a list of cwt.Variable or a dict.
print(process.output)
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
