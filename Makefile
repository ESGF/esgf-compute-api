CACHE_PATH ?= $(PWD)/cache
OUTPUT_PATH ?= $(PWD)/output
TARGET ?= builder

BASE_IMAGE := continuumio/miniconda3:4.8.2
TARGET := builder
BUILD_CONTEXT := .
BUILD_DOCKERFILE := .

BUILDKIT_ARGS = /usr/bin/buildctl-daemonless.sh \
								build \
								--frontend=dockerfile.v0 \
								--local context=$(BUILD_CONTEXT) \
								--local dockerfile=$(BUILD_DOCKERFILE) \
								$(CACHE_ARG) $(OUTPUT_ARG) $(EXTRA_ARG)

ifeq ($(shell which buildctl-daemonless.sh),)
else
BUILD = $(SHELL) $(BUILDKIT_ARGS)
endif

CACHE_ARG := --export-cache type=local,dest=$(CACHE_PATH),mode=max \
				--import-cache type=local,src=$(CACHE_PATH)

EXTRA_ARG := --opt build-arg:BASE_IMAGE=$(BASE_IMAGE)
EXTRA_ARG += --opt target=$(TARGET)

ifeq ($(TARGET),publish)
EXTRA_ARG += --opt build-arg:CONDA_TOKEN=$(CONDA_TOKEN)
endif

ifeq ($(OUTPUT_TYPE),docker)
OUTPUT_ARG := --output type=docker,name=dev-api,dest=$(OUTPUT_PATH)/image.tar

POST_CMD := cat $(OUTPUT_PATH)/image.tar | docker load
else ifeq ($(TARGET),testresult)
OUTPUT_ARG := --output type=local,dest=$(OUTPUT_PATH)
endif

CONDA := $(shell find /opt/conda/bin ${HOME}/conda/bin -type f -iname 'conda' 2>/dev/null)
CONDA_BIN := $(patsubst %/conda,%,$(CONDA))

.PHONY: docker-build-docs
docker-build-docs:
	docker run -it --rm \
		-v $(PWD):/src \
		-w /src \
		--entrypoint /bin/bash \
		$(BASE_IMAGE) \
		-c "apt update && apt install make && make build-docs"

.PHONY: build-docs
build-docs:
	$(CONDA) install -y -c conda-forge python m2r2 "sphinx<=3.2" recommonmark oauthlib owslib

	pip install -e .

	@make -C docsrc/ html SPHINX_OPTS=-vvvv

	@cp -a docsrc/build/html/. docs/

.PHONY: docker-build
docker-build:
	docker run \
		-it --rm \
		--privileged \
		-v $(PWD):/build -w /build \
		-v $(CACHE_PATH):$(CACHE_PATH) \
		-v $(OUTPUT_PATH):$(OUTPUT_PATH) \
		--entrypoint=/bin/sh \
		moby/buildkit:master \
		-c "apk add make && make build"

	$(POST_CMD)

.PHONY: build
build:
	$(BUILDKIT_ARGS)
