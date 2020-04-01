.PHONY: build

ifeq ($(shell which buildctl-daemonless.sh),)
BUILD = docker run \
				-it --rm \
				--privileged \
				-v $(PWD):/build -w /build \
				--entrypoint=/bin/sh \
				moby/buildkit:master
else
BUILD = $(SHELL)
endif

build: EXTRA = --opt build-arg:CONDA_TOKEN=$(CONDA_TOKEN)
build:
	$(BUILD) build.sh $(EXTRA)
