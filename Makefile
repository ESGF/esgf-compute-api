.DEFAULT_GOAL := build

GIT_REV := $(shell git rev-parse --short HEAD)
GIT_BRANCH := $(shell git rev-parse --abbrev-ref HEAD)

TARGET ?= build
CACHE_PATH ?= $(PWD)/cache
OUTPUT_PATH ?= $(PWD)/output
BASE_IMAGE = condaforge/mambaforge:4.9.2-5

CACHE_ARG = --import-cache type=local,src=$(CACHE_PATH) \
						--export-cache type=local,dest=$(CACHE_PATH),mode=max

CONFIG_ARG = --opt build-arg:BASE_IMAGE=$(BASE_IMAGE) \
	--opt build-arg:CONDA_TOKEN=$(CONDA_TOKEN)

ifeq ($(TARGET),testresult)
OUTPUT_ARG = --output type=local,dest=$(OUTPUT_PATH)
endif

BUILD_ARG = /usr/bin/buildctl-daemonless.sh \
						build \
						--frontend dockerfile.v0 \
						--local context=$(PWD)/$(DOCKERFILE) \
						--local dockerfile=$(PWD)/$(DOCKERFILE) \
						--opt target=$(TARGET) \
						$(CACHE_ARG) \
						$(CONFIG_ARG) \
						$(OUTPUT_ARG)

ifeq ($(shell which buildctl-daemonless.sh 2>/dev/null),)
BUILD = docker run -it --rm \
				--privileged \
				--group-add $(shell id -g) \
				-v $(PWD):$(PWD) \
				-w $(PWD) \
				--entrypoint=/bin/sh \
				moby/buildkit:master \
				$(BUILD_ARG)
else
BUILD = /bin/sh \
				$(BUILD_ARG)
endif

.PHONY: upload
upload: TARGET := publish
upload: build

.PHONY: build
build:
	$(BUILD_PRE)

	$(BUILD)

	$(BUILD_POST)
