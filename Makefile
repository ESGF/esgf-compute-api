build:
	docker run -it --rm \
		-v $(PWD):/data -w /data \
		--privileged \
		--entrypoint=/bin/sh \
		-e CONDA_TOKEN=$(CONDA_TOKEN) \
		moby/buildkit:master \
		build.sh
