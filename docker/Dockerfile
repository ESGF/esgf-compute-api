FROM continuumio/miniconda:4.3.27

ARG BRANCH=master

ENV JUPYTER_MODULE=notebook

RUN conda install -c conda-forge jupyterlab nb_conda_kernels && \
	conda clean -y --all

COPY environment.yaml environment.yaml

RUN apt-get update && \
	apt-get install --no-install-recommends -y build-essential && \
	conda env create -n esgf-compute-api --file environment.yaml && \
	conda clean -y --all && \
	apt-get purge -y --auto-remove build-essential && \
	rm -rf /var/lib/apt/lists/*

RUN git clone --branch=$BRANCH --depth=1 https://github.com/ESGF/esgf-compute-api && \
	cd esgf-compute-api && \
	PATH=/opt/conda/envs/esgf-compute-api/bin:$PATH pip install -r requirements.txt && \
	PATH=/opt/conda/envs/esgf-compute-api/bin:$PATH python setup.py install

EXPOSE 9999

ENTRYPOINT ["/bin/sh", "-c", "jupyter $JUPYTER_MODULE --ip 0.0.0.0 --port 9999 --allow-root --notebook-dir /esgf-compute-api/examples"]
