ARG BASE_IMAGE
FROM $BASE_IMAGE as builder

RUN conda update -n base -c defaults conda && \
      conda install -c conda-forge conda-smithy conda-build anaconda-client

WORKDIR /build

RUN conda smithy ci-skeleton esgf-compute-api

COPY meta.yaml recipe/
COPY cwt/ recipe/cwt
COPY setup.py recipe/

RUN conda config --set ssl_verify false && \
      conda smithy rerender && \
      conda build recipe/ -m .ci_support/linux_64_.yaml -c conda-forge --output-folder channel/ && \
      conda index channel/

FROM $BASE_IMAGE as docs

RUN conda create -y -c conda-forge m2r2 sphinx recommonmark && \
      make -C dodsrc/ html && \
      cp -a dodsrc/build/html/. docs/

FROM scratch as testresult

COPY --from=builder /output/coverage.xml .
COPY --from=builder /output/unittest.xml .
COPY --from=builder /build/channel/noarch/*.tar.bz2 .

FROM builder as publish

ARG CONDA_TOKEN
ENV CONDA_TOKEN $CONDA_TOKEN

COPY --from=builder /build/channel/noarch/*.tar.bz2 .

RUN anaconda config --set ssl_verify false && \
      anaconda -t ${CONDA_TOKEN} upload -u cdat --skip-existing *.tar.bz2
