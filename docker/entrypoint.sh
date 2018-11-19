#! /bin/bash

conda install -y -c conda-forge -c cdat esgf-compute-api=${API_VERSION} cdms2 mesalib vcs

[ -z "${PIP_EXTRA_PACKAGES}" ] && pip install ${PIP_EXTRA_PACKAGES}

[ -z "${CONDA_EXTRA_PACKAGES}" ] && conda install ${CONDA_EXTRA_PACKAGES}

jupyter lab --ip 0.0.0.0 --port 9999 --allow-root --notebook-dir /esgf-compute-api/examples
