.PHONY: build

CACHE_PATH := $(PWD)/cache
OUTPUT_PATH := $(PWD)/output

ifeq ($(shell which buildctl-daemonless.sh),)
BUILD := docker run \
				-it --rm \
				--privileged \
				-v $(PWD):/build -w /build \
				-v $(CACHE_PATH):$(CACHE_PATH) \
				-v $(OUTPUT_PATH):$(OUTPUT_PATH) \
				--entrypoint=/bin/sh \
				moby/buildkit:master
else
BUILD := $(SHELL)
endif

BASE_IMAGE := continuumio/miniconda3:4.8.2
TARGET := builder

CACHE_ARG := --export-cache type=local,dest=$(CACHE_PATH),mode=max \
				--import-cache type=local,src=$(CACHE_PATH)

EXTRA_ARG := --opt build-arg:BASE_IMAGE=$(BASE_IMAGE)

ifeq ($(TARGET),publish)
EXTRA_ARG += --opt build-arg:CONDA_TOKEN=$(CONDA_TOKEN)
endif

EXTRA_ARG += --opt target=$(TARGET)

OUTPUT_ARG := --output type=docker,name=dev-api,dest=$(OUTPUT_PATH)/image.tar

POST_CMD := cat $(OUTPUT_PATH)/image.tar | docker load

dev-env:
	conda create -n api-dev -c conda-forge pytest pytest-cov pytest-mock mock
	conda activate api-dev
	pip install -e .

build:
	$(BUILD) build.sh $(CACHE_ARG) $(OUTPUT_ARG) $(EXTRA_ARG)

	$(POST_CMD)
