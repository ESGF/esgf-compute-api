CACHE_PATH ?= $(PWD)/cache
OUTPUT_PATH ?= $(PWD)/output
BUILD_TYPE ?= buildkit

BASE_IMAGE := continuumio/miniconda3:4.8.2
TARGET := builder
BUILD_CONTEXT := .
BUILD_DOCKERFILE := .

ifeq ($(findstring buildctl-daemonless.sh,$(shell which buildctl-daemonless.sh)),buildctl-daemonless.sh)
BUILD_TYPE := buildkit
BUILD = $(SHELL) \
				/usr/bin/buildctl-daemonless.sh \
				build \
				--frontend=dockerfile.v0 \
				--local context=$(BUILD_CONTEXT) \
				--local dockerfile=$(BUILD_DOCKERFILE) \
				$(CACHE_ARG) $(OUTPUT_ARG) $(EXTRA_ARG)
else ifeq ($(BUILD_TYPE),buildkit)
BUILD_TYPE := buildkit
BUILD = docker run \
				-it --rm \
				--privileged \
				-v $(PWD):/build -w /build \
				-v $(CACHE_PATH):$(CACHE_PATH) \
				-v $(OUTPUT_PATH):$(OUTPUT_PATH) \
				--entrypoint=/bin/sh \
				moby/buildkit:master \
				/usr/bin/buildctl-daemonless.sh \
				build \
				--frontend=dockerfile.v0 \
				--local context=$(BUILD_CONTEXT) \
				--local dockerfile=$(BUILD_DOCKERFILE) \
				$(CACHE_ARG) $(OUTPUT_ARG) $(EXTRA_ARG)
else
BUILD = docker build \
				-t compute-api \
				--build-arg=BASE_IMAGE=$(BASE_IMAGE) \
				$(EXTRA_ARG) .
endif

ifeq ($(BUILD_TYPE),buildkit)
CACHE_ARG := --export-cache type=local,dest=$(CACHE_PATH),mode=max \
				--import-cache type=local,src=$(CACHE_PATH)

EXTRA_ARG := --opt build-arg:BASE_IMAGE=$(BASE_IMAGE)
endif

ifeq ($(TARGET),publish)
ifeq ($(BUILD_TYPE),buildkit)
EXTRA_ARG += --opt build-arg:CONDA_TOKEN=$(CONDA_TOKEN)
else
EXTRA_ARG += --build-arg=CONDA_TOKEN=$(CONDA_TOKEN)
endif
endif

ifeq ($(BUILD_TYPE),buildkit)
EXTRA_ARG += --opt target=$(TARGET)
else
EXTRA_ARG += --target=$(TARGET)
endif

ifeq ($(BUILD_TYPE),buildkit)
ifeq ($(OUTPUT_TYPE),docker)
OUTPUT_ARG := --output type=docker,name=dev-api,dest=$(OUTPUT_PATH)/image.tar

POST_CMD := cat $(OUTPUT_PATH)/image.tar | docker load
else ifeq ($(TARGET),testresult)
OUTPUT_ARG := --output type=local,dest=$(OUTPUT_PATH)
endif
endif

CONDA := $(shell find /opt/**/bin ${HOME}/**/bin -type f -iname 'conda' 2>/dev/null)
CONDA_BIN := $(patsubst %/conda,%,$(CONDA))

.PHONY: build-docs
build-docs:
	$(CONDA_BIN)/activate api-dev; \
		make -C docsrc/ html; \
		cp -a docsrc/build/html/. docs/

.PHONY: dev-env
dev-env: BUILD_DEPS := owslib oauthlib
dev-env: DEV_DEPS := pytest pytest-cov pytest-mock mock m2r2 sphinx recommonmark
dev-env:
	$(CONDA_BIN)/activate base; \
		$(CONDA) env remove -y -n api-dev; \
		$(CONDA) create -y -n api-dev -c conda-forge $(DEV_DEPS) $(BUILD_DEPS)

	$(CONDA_BIN)/activate api-dev; \
		pip install -e .

.PHONY: build
build:
	$(BUILD)

	$(POST_CMD)
