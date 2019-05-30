FROM continuumio/miniconda:4.6.14 as base

COPY . /compute-api

WORKDIR /compute-api

ENV TINI_VERSION v0.18.0

RUN curl https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini -o /tini && \
      chmod +x /tini

CMD ["/tini", "--"]

FROM base as builder

RUN conda install -c conda-forge -y conda-build=3.17.8 && \
      conda build -c conda-forge conda/

FROM base as dev

RUN conda install -c conda-forge -y conda-build=3.17.8 ipython && \
      conda develop .

ENTRYPOINT ["/bin/bash"]

FROM continuumio/miniconda:4.6.14 as prod

COPY --from=builder /opt/conda/conda-bld/noarch/* /opt/conda/conda-bld/noarch/

RUN conda install -c conda-forge --use-local esgf-compute-api ipython

ENTRYPOINT ["ipython"]

FROM prod as jupyterlab

RUN conda install -c conda-forge jupyterlab

COPY docker/jupyter_notebook_config.json /root/.jupyter/

EXPOSE 8888

COPY --from=base /compute-api/examples* /compute-api/examples/

ENTRYPOINT ["jupyter", "lab", "--ip", "0.0.0.0", "--port", "8888", "--allow-root", "--notebook-dir", "/compute-api/examples"]
