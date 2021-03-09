# ESGF Compute end-user API
> The ESGF Compute end-user API provides an object-oriented climatology package
to access large scale computational resources through the Web Processing
Service interface standard.

Supported WPS version: 1.0.0

### Documentation

Documentation can be found on [here](https://esgf.github.com/esgf-compute-api).

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

```python
import cwt

# Create a variable from an OpenDAP url and the name of the variable.
tas = cwt.Variable('...', var_name='...')

# Initialize the client with the url to the WPS endpoint and the Token/API key.
wps = cwt.WPSClient('http://.../wps', compute_token='...')

# Select the process to execut.
process = wps.CDAT.subset(tas)

# Execut the process.
wps.execute(process)

# Wait for the process to complete, this will print status message to the console.
process.wait()

# Prints the output of the process which is either an instance of cwt.Variable, a list of cwt.Variable or a dict.
print(process.output)
```

### Example

Jupyter Notebook cotnaining examples can be found [here](examples/)

### Compatibility

Compatibility document can be found on [here](docs/source/cwt.compat.rst)
