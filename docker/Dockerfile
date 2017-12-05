FROM continuumio/miniconda:4.3.27

RUN apt-get update --fix-missing && \
	apt-get install -y build-essential && \
	conda install -y -c conda-forge -c uvcdat mesalib esgf-compute-api \
	jupyter nb_conda_kernels cdms2 vcs && \
	conda clean -y --all && \
	apt-get autoremove -y && \
	apt-get autoclean -y

RUN git clone --depth=1 https://github.com/ESGF/esgf-compute-api 

EXPOSE 9999

ENTRYPOINT ["jupyter", "notebook"]

CMD ["--ip", "0.0.0.0", "--port", "9999", "--allow-root", "--notebook-dir", "/esgf-compute-api/examples"]
