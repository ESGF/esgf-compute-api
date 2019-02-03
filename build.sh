#! /bin/bash

set -e

function usage() {
  echo "${0} --new --push-conda --push-docker --docker-args=<args>"
  echo ""
  echo "Builds conda package and docker container from BRANCH."
  echo ""
  echo "Options:"
  echo "      --new:              Increments the conda build number"
  echo "      --push-conda:       Push conda package"
  echo "      --build-docker:     Build docker image"
  echo "      --push-docker:      Push docker image"
  echo "      --docker-args:      Arguments to pass docker build command"
  echo "      --version:          Override version"
  echo "  -h, --help:             Prints usage"
  echo ""
}

PUSH_CONDA=0
BUILD_DOCKER=0
PUSH_DOCKER=0
NEW=0
DOCKER_ARGS=""

while [[ ${#} -gt 0 ]]
do
  NAME=${1} && shift

  case "${NAME}" in
    --push-conda)
      PUSH_CONDA=1
      ;;
    --build-docker)
      BUILD_DOCKER=${1} && shift
      ;;
    --push-docker)
      PUSH_DOCKER=1
      ;;
    --new)
      NEW=1
      ;;
    --docker-args)
      DOCKER_ARGS=${1} && shift
      ;;
    --version)
      VERSION=${1} && shift
      ;;
    -h|--help|*):
      usage

      exit 0
  esac
done

BRANCH=$(git branch | grep \* | cut -d " " -f 2)

[[ -z "${VERSION}" ]] && VERSION=${BRANCH##*/}

read -p "Building from branch \"${BRANCH}\" tagged as version \"${VERSION}\" [ENTER]: "

git checkout ${BRANCH}

BUILD_DIR=${PWD}/.build

BUILD=$(conda search -c cdat esgf-compute-api | grep ${VERSION} | tail -n1 | tr -s " " | cut -d " " -f 3 | cut -d "_" -f 2)

if [[ -z ${BUILD} ]]; then
  BUILD=0
else
  if [[ ${NEW} -eq 1 ]]; then
    BUILD=$((++BUILD))
  fi
fi

sed -i "s|\(.*version: \).*|\1\"${VERSION}\"|" conda/meta.yaml

sed -i "s|\(.*git_rev: \).*|\1${BRANCH}|" conda/meta.yaml

sed -i "s|\(__version__ = \).*|\1\'${VERSION}\'|" cwt/__init__.py

sed -i "s|\(.*jasonb87/cwt_api:\).*|\1${VERSION}|" docs/source/cwt_docker.md

conda build -c conda-forge -c cdat conda/

if [[ ${PUSH_CONDA} -eq 1 ]]; then
  anaconda login

  #anaconda upload -u cdat ${PACKAGE_OSX}
fi

if [[ ${BUILD_DOCKER} -eq 1 ]]; then
  docker build ${DOCKER_ARGS} -t jasonb87/cwt_api:${VERSION} -f docker/Dockerfile .

  if [[ ${PUSH_DOCKER} -eq 1 ]]; then
    docker login

    docker push jasonb87/cwt_api:${VERSION}
  fi
fi
