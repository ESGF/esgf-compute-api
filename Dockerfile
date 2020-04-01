FROM continuumio/miniconda3:4.6.14 as builder

RUN conda update -n base -c defaults conda && \
      conda install conda-build anaconda-client

WORKDIR /build

COPY meta.yaml meta.yaml
COPY cwt/ cwt/
COPY setup.py setup.py

RUN conda build -c conda-forge .

FROM continuumio/miniconda3:4.6.14 as production

WORKDIR /

COPY --from=builder /opt/conda/conda-bld /opt/conda/conda-bld
COPY --from=builder /opt/conda/pkgs /opt/conda/pkgs

RUN conda install -c conda-forge --use-local esgf-compute-api jupyterlab cdms2 matplotlib

COPY jupyter_notebook_config.json .

EXPOSE 8080

ENTRYPOINT ["/tini", "--"]

CMD ["jupyter", "lab", "--ip", "0.0.0.0", "--port", "8080", "--allow-root", "--config", "./jupyter_notebook_config.json"]

FROM scratch as testresult

COPY --from=builder /output/coverage.xml .
COPY --from=builder /output/unittest.xml .

FROM builder as publish

ARG CONDA_TOKEN
ENV CONDA_TOKEN $CONDA_TOKEN

RUN anaconda config --set ssl_verify false && \
      anaconda -t ${CONDA_TOKEN} upload -u cdat --skip-existing $(conda build -c conda-forge . --output)
