#! /bin/bash

function usage() {
  echo -e "./${0} version build git_branch [--push]"
}

[[ $# -lt 3 ]] && usage && exit 1

VERSION=$1
shift

BUILD=$1
shift

GIT_BRANCH=$1
shift

PUSH=0

while [[ $# -gt 0 ]]
do
  NAME=$1
  shift

  case "${NAME}" in
    --push)
      PUSH=1
      ;;
  esac
done

./bump_version.sh ${VERSION} ${GIT_BRANCH} ${BUILD}

conda build -c conda-forge --output-folder ${PWD}/_build conda/

if [[ $PUSH -eq 1 ]]
then
  anaconda login

  PACKAGE=$(conda build -c conda-forge --output-folder ${PWD}/_build --output conda/)

  conda convert -p osx-64 --output-dir ${PWD}/_build ${PACKAGE}

  anaconda upload -u cdat --force ${PACKAGE}

  PACKAGE_OSX=$(echo ${PACKAGE} | sed "s/linux-64/osx-64/")

  anaconda upload -u cdat --force ${PACKAGE_OSX}
fi
