FROM continuumio/miniconda3:4.6.14 as builder

RUN conda install conda-build

WORKDIR /src

COPY meta.yaml .
COPY cwt/ cwt/
COPY setup.py .

RUN conda build -c conda-forge .

FROM continuumio/miniconda3:4.6.14 as production

WORKDIR /

COPY --from=builder /opt/conda/conda-bld /opt/conda/conda-bld
COPY --from=builder /opt/conda/pkgs /opt/conda/pkgs

RUN conda install -c conda-forge --use-local esgf-compute-api jupyterlab cdms2 matplotlib

COPY jupyter_notebook_config.json .

ENV TINI_VERSION v0.18.0

ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini

RUN chmod +x /tini

EXPOSE 8080

ENTRYPOINT ["/tini", "--"]

CMD ["jupyter", "lab", "--ip", "0.0.0.0", "--port", "8080", "--allow-root", "--config", "./jupyter_notebook_config.json"]

FROM production as testing

WORKDIR /testing

RUN conda install -c conda-forge pytest pytest-mock pytest-cov mock

COPY cwt/ cwt/

RUN pytest -vvv --cov=cwt --cov-report=html:coverage/ --cov-report=xml:coverage.xml --junit-xml=unittest.xml

FROM scratch as testresult

COPY --from=testing /testing/coverage/ coverage/
COPY --from=testing /testing/coverage.xml .
COPY --from=testing /testing/unittest.xml .

FROM builder as publish

ARG CONDA_USERNAME
ENV CONDA_USERNAME $CONDA_USERNAME
ARG CONDA_PASSWORD
ENV CONDA_PASSWORD $CONDA_PASSWORD

RUN conda install anaconda-client

RUN anaconda login --username ${CONDA_USERNAME} --password ${CONDA_PASSWORD}
      
RUN anaconda upload -u cdat --skip $(conda build -c conda-forge . --output)
