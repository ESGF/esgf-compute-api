#! /bin/bash

function usage() {
  echo "${0} --new --push"
  echo ""
  echo "This will build the conda package using the current build number"
  echo ""
  echo "Options:"
  echo "      --new:      Increments the build number"
  echo "      --push:     Pushes new build to \"cdat\" channel"
  echo "  -h, --help:     Prints usage"
  echo ""
}

PUSH=0
NEW=0

while [[ ${#} -gt 0 ]]
do
  NAME=${1} && shift

  case "${NAME}" in
    --push)
      PUSH=1
      ;;
    --new)
      NEW=1
      ;;
    -h|--help|*):
      usage

      exit 0
  esac
done

VERSION=$(git branch | grep \* | cut -d " " -f 2)

VERSION=${VERSION##*/}

BUILD_DIR=${PWD}/.build

BUILD=$(conda search -c cdat esgf-compute-api | grep ${VERSION} | tail -n1 | tr -s " " | cut -d " " -f 3 | cut -d "_" -f 2)

if [[ -z ${BUILD} ]]; then
  BUILD=0
else
  if [[ ${NEW} -eq 1 ]]; then
    BUILD=$((++BUILD))
  fi
fi

echo ""

sed "s/\(.*number: \).*/\1${BUILD}/" conda/meta.yaml 

echo ""

read -p "Confirm the conda meta file [ENTER]: "

sed -i.bak "s/\(.*number: \).*/\1${BUILD}/" conda/meta.yaml 

conda build -c conda-forge -c cdat --output-folder ${BUILD_DIR} conda/

if [[ ${PUSH} -eq 1 ]]
then
  anaconda login

  PACKAGE=$(conda build -c conda-forge --output-folder ${BUILD_DIR} --output conda/)

  conda convert -p osx-64 --output-dir ${BUILD_DIR} ${PACKAGE}

  anaconda upload -u cdat --force ${PACKAGE}

  PACKAGE_OSX=$(echo ${PACKAGE} | sed "s/linux-64/osx-64/")

  anaconda upload -u cdat --force ${PACKAGE_OSX}
fi
