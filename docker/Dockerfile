FROM continuumio/miniconda3:4.6.14 as builder

ARG COMPUTE_API_VER
ENV COMPUTE_API_VER=${COMPUTE_API_VER}

WORKDIR /src

COPY conda conda/
COPY cwt cwt/
COPY setup.py .

RUN echo "__version__ = '${COMPUTE_API_VER}'" > cwt/_version.py && \
      conda install conda-build anaconda-client && \
      conda build -c conda-forge conda/

ENTRYPOINT ["tini", "--"]

FROM builder as dev

RUN apt-get update && \
      apt-get install -y --no-install-recommends vim-nox && \
      rm -rf /var/lib/apt/lists/* && \
      conda install -c conda-forge --use-local --only-deps esgf-compute-api && \
      conda install -c conda-forge -y flake8 pytest pytest-mock pytest-cov mock && \
      pip install -e .

FROM continuumio/miniconda3:4.6.14

WORKDIR /

COPY --from=builder /opt/conda/conda-bld/noarch /opt/conda/conda-bld/noarch/
COPY --from=builder /opt/conda/pkgs /opts/conda/pkgs/

COPY examples /examples/
COPY docker/jupyter_notebook_config.json /root/.jupyter/

RUN conda install -c conda-forge -c cdat --use-local esgf-compute-api jupyterlab mesalib nomkl vcs cdms2 && \
      conda clean -y -a

EXPOSE 8888

ENTRYPOINT ["tini", "--"]

CMD ["/bin/bash", "-c", "jupyter lab --ip 0.0.0.0 --port 8888 --allow-root --notebook-dir /examples"]
