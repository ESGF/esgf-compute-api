FROM continuumio/miniconda:4.3.27

ARG GIT_BRANCH=master

ARG API_VERSION=2.1.0

RUN git clone https://github.com/ESGF/esgf-compute-api && \
      cd esgf-compute-api && \
      git checkout ${GIT_BRANCH}

RUN conda install -c conda-forge jupyterlab nb_conda_kernels && \
	conda clean -y --all && \
  rm -rf /opt/conda/pkgs/*

RUN apt-get update && \
	apt-get install --no-install-recommends -y build-essential && \
	rm -rf /usr/share/doc/ && \
	rm -rf /usr/share/man/ && \
	rm -rf /usr/share/locale && \
	rm -rf /var/lib/apt/lists/*

COPY jupyter_notebook_config.json /root/.jupyter/jupyter_notebook_config.json
COPY entrypoint.sh entrypoint.sh

EXPOSE 9999

ENTRYPOINT ["./entrypoint.sh"]
