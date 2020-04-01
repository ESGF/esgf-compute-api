.PHONY: build

ifeq ($(shell which buildctl-daemonless.sh),)
BUILD = docker run \
				-it --rm \
				--privileged \
				-v $(PWD):/build -w /build \
				-v $(PWD)/cache:/cache \
				-v $(PWD)/output:/output \
				--entrypoint=/bin/sh \
				moby/buildkit:master
else
BUILD = $(SHELL)
endif

TARGET = publish

CACHE = --export-cache type=local,dest=/cache,mode=max \
				--import-cache type=local,src=/cache

EXTRA = --opt target=$(TARGET) \
				--opt build-arg:CONDA_TOKEN=$(CONDA_TOKEN)

ifeq ($(TARGET),production)
IMAGE = $(if $(REGISTRY),$(REGISTRY)/)compute-api
VERSION = 2.2.3
OUTPUT = --output type=image,name=$(IMAGE):$(VERSION),push=true
else ($(TARGET),testresult)
ifeq ($(shell which buildctl-daemonless.sh),)
OUTPUT = --output type=local,dest=/output
else
OUTPUT = --output type=local,dest=output
endif
endif

build:
	$(BUILD) build.sh $(EXTRA) $(CACHE) $(OUTPUT)
