FROM continuumio/miniconda:4.3.27

RUN apt-get update && \
	apt-get install --no-install-recommends -y build-essential && \
	rm -rf /var/lib/apt/lists/*

RUN conda install -c conda-forge jupyterlab nb_conda_kernels nodejs && \
      conda create -n esgf-compute-api -c conda-forge -c cdat python=2 nomkl mesalib cdms2 vcs ipykernel && \
      conda clean -y --all && \
      rm -rf /opt/conda/pkgs/*

COPY docker/jupyter_notebook_config.json /root/.jupyter/jupyter_notebook_config.json

COPY docker/entrypoint.sh entrypoint.sh

COPY . /esgf-compute-api

WORKDIR /esgf-compute-api

RUN pip install -e .

EXPOSE 9999

ENTRYPOINT ["./entrypoint.sh"]
