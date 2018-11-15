# Docker CWT API

The docker CWT API image has the following libraries installed:

* [esgf-compute-api](https://github.com/ESGF/esgf-compute-api)
* [Jupyter Notebook](https://jupyter.org)
* [CDMS2](https://uvcdat.llnl.gov/documentation/cdms/cdms.html)
* [VCS](https://uvcdat.llnl.gov/documentation/vcs/vcs.html)

After pulling and running the image, you can access jupyter notebook from
http://localhost:9999. The access token can be retrieved from the terminal
after running the image.

# Running the docker image

```
docker run -it -p 9999:9999 jasonb87/cwt_api:latest
```
