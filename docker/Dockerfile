FROM continuumio/miniconda3:4.6.14 as builder

ARG VER

COPY . /compute-api

WORKDIR /compute-api

ENV VER=${VER}

RUN echo "__version__ = '${VER}'" > cwt/_version.py && \
      conda install -c conda-forge conda-build && \
      conda build -c conda-forge conda/

FROM builder as uploader

RUN conda install -c conda-forge anaconda-client 

ENTRYPOINT ["/bin/bash", "-c"]

CMD ["anaconda login && anaconda upload /opt/conda/build-pkg/noarch/esgf-compute-api-${VER}-py_0.tar.bz2 -u cdat"]

FROM continuumio/miniconda3:4.6.14 as prod

ARG VER

ENV VER=${VER}

WORKDIR /

COPY --from=builder /opt/conda/conda-bld/noarch/* /opt/conda/conda-bld/noarch/

COPY --from=builder /compute-api/examples/* /examples/

RUN conda install -c cdat -c conda-forge --use-local esgf-compute-api=${VER} jupyterlab ipython mesalib nomkl vcs cdms2 && \
     rm -rf /opt/conda/conda-bld

ENV TINI_VERSION v0.18.0

RUN curl https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini -o /tini && \
      chmod +x /tini

COPY docker/jupyter_notebook_config.json /root/.jupyter/

EXPOSE 8888

ENTRYPOINT ["tini", "--"]

CMD ["/bin/bash", "-c", "jupyter lab --ip 0.0.0.0 --port 8888 --allow-root --notebook-dir /examples"]
