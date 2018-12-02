# Docker CWT API

The CWT API docker image has the following libraries installed:

* [esgf-compute-api](https://github.com/ESGF/esgf-compute-api)
* [Jupyter Notebook](https://jupyter.org)
* [CDMS2](https://uvcdat.llnl.gov/documentation/cdms/cdms.html)
* [VCS](https://uvcdat.llnl.gov/documentation/vcs/vcs.html)

# Running the docker image

### Jupyter Lab

> Replace the {version} with the version of the API you wish to use.

```
docker run -d -p 9999:9999 jasonb87/cwt_api:{version}
```

> After running the image open http://127.0.0.1:9999, the password is "esgf".
