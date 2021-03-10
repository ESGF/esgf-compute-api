ARG BASE_IMAGE
FROM $BASE_IMAGE as build

RUN mamba install -y -n base -c conda-forge boa anaconda-client

WORKDIR /build

COPY feedstock/ feedstock/
COPY cwt/ feedstock/recipe/cwt/
COPY setup.py feedstock/recipe/setup.py

RUN mamba mambabuild feedstock/recipe \
      -m feedstock/.ci_support/linux_64_.yaml \
      -c conda-forge \
      --output-folder channel/ && \
      conda index channel/

FROM scratch as testresult

COPY --from=build /output/coverage.xml .
COPY --from=build /output/unittest.xml .
COPY --from=build /build/channel/noarch/*.tar.bz2 .

FROM build as publish

ARG CONDA_TOKEN
ENV CONDA_TOKEN $CONDA_TOKEN

COPY --from=build /build/channel/noarch/*.tar.bz2 .

RUN anaconda config --set ssl_verify false && \
      anaconda -t ${CONDA_TOKEN} upload -u cdat --skip-existing *.tar.bz2
