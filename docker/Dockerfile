FROM continuumio/miniconda:4.3.27

RUN apt-get update && \
	apt-get install --no-install-recommends -y build-essential && \
	rm -rf /var/lib/apt/lists/*

COPY environment.yaml environment.yaml

RUN conda install -c conda-forge jupyterlab nb_conda_kernels nodejs && \
      conda create -n esgf-compute-api -c conda-forge -c cdat python=2 nomkl mesalib cdms2 vcs ipykernel && \
      conda env update -n esgf-compute-api -f environment.yml && \
      conda clean -y --all && \
      rm environment.yml && \
      rm -rf /opt/conda/pkgs/*

COPY docker/jupyter_notebook_config.json /root/.jupyter/jupyter_notebook_config.json

COPY docker/entrypoint.sh entrypoint.sh

COPY . /esgf-compute-api

WORKDIR /esgf-compute-api

RUN PATH=/opt/conda/envs/esgf-compute-api/bin:$PATH pip install -e .

WORKDIR /esgf-compute-api/docker

EXPOSE 9999

ENTRYPOINT ["./entrypoint.sh"]
