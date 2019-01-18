#! /bin/bash

function usage() {
  echo "${0} --new --push-conda --push-docker"
  echo ""
  echo "Builds conda package and docker container from BRANCH."
  echo ""
  echo "Options:"
  echo "      --new:      Increments the conda build number"
  echo "      --push:     Pushes the conda package and docker container"
  echo "  -h, --help:     Prints usage"
  echo ""
}

PUSH_CONDA=0
PUSH_DOCKER=0
NEW=0

while [[ ${#} -gt 0 ]]
do
  NAME=${1} && shift

  case "${NAME}" in
    --push-conda)
      PUSH_CONDA=1
      ;;
    --push-docker)
      PUSH_DOCKER=1
      ;;
    --new)
      NEW=1
      ;;
    -h|--help|*):
      usage

      exit 0
  esac
done

BRANCH=$(git branch | grep \* | cut -d " " -f 2)

read -p "Building from branch \"${BRANCH}\" [ENTER]: "

git checkout ${BRANCH}

VERSION=${BRANCH##*/}

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

sed -i "s|\(.*jasonb87/cwt_api:\)|\1${VERSION}|" docs/source/cwt_docker.md

conda build -c conda-forge -c cdat --output-folder ${BUILD_DIR} conda/

docker build -t jasonb87/cwt_api:${VERSION} -f docker/Dockerfile .

if [[ ${PUSH_CONDA} -eq 1 ]]; then
  anaconda login

  PACKAGE=$(conda build -c conda-forge --output-folder ${BUILD_DIR} --output conda/)

  conda convert -p osx-64 --output-dir ${BUILD_DIR} ${PACKAGE}

  anaconda upload -u cdat --force ${PACKAGE}

  PACKAGE_OSX=$(echo ${PACKAGE} | sed "s/linux-64/osx-64/")

  anaconda upload -u cdat --force ${PACKAGE_OSX}
fi

if [[ ${PUSH_DOCKER} -eq 1 ]]; then
  docker login

  docker push jasonb87/cwt_api:${VERSION}
fi
