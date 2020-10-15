ARG BASE_IMAGE
FROM $BASE_IMAGE as builder

RUN conda update -n base -c defaults conda && \
      conda install -c conda-forge conda-smithy conda-build anaconda-client

WORKDIR /build

RUN conda smithy ci-skeleton esgf-compute-api

COPY meta.yaml recipe/
COPY cwt/ recipe/cwt
COPY setup.py recipe/

RUN conda smithy rerender && \
      conda build recipe/ -m .ci_support/linux_64_.yaml -c conda-forge --output-folder channel/ && \
      conda index channel/

FROM $BASE_IMAGE as jupyterlab

WORKDIR /

COPY jupyter_notebook_config.json .
COPY --from=builder /build/channel /channel 

RUN conda install -c conda-forge -c file:///channel jupyterlab esgf-compute-api

EXPOSE 8080

ENTRYPOINT ["/tini", "--"]

CMD ["jupyter", "lab", "--ip", "0.0.0.0", "--port", "8080", "--allow-root", "--config", "./jupyter_notebook_config.json"]

FROM scratch as testresult

COPY --from=builder /output/coverage.xml .
COPY --from=builder /output/unittest.xml .

FROM builder as publish

ARG CONDA_TOKEN
ENV CONDA_TOKEN $CONDA_TOKEN

COPY --from=builder /build/channel/noarch/*.tar.bz2 .

RUN anaconda config --set ssl_verify false && \
      anaconda -t ${CONDA_TOKEN} upload -u cdat --skip-existing *.tar.bz2
