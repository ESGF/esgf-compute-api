# Docker CWT API

The CWT API docker image has the following libraries installed:

* [esgf-compute-api](https://github.com/ESGF/esgf-compute-api)
* [Jupyter Notebook](https://jupyter.org)
* [CDMS2](https://uvcdat.llnl.gov/documentation/cdms/cdms.html)
* [VCS](https://uvcdat.llnl.gov/documentation/vcs/vcs.html)

# Running the docker image

> After running the docker image, follow the instructions in the console output.

### Jupyter Notebook

```
docker run -it -p 9999:9999 jasonb87/cwt_api:latest
```

### Jupyter Lab

```
docker run -it -p 9999:9999 -e JUPYTER_MODULE=lab jasonb87/cwt_api:latest
```
