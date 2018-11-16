#! /bin/bash

PUSH=0

while [[ $# -gt 0 ]]
do
  ARG=$1

  shift

  case $ARG in
    --push)
      PUSH=1
      ;;
    --git-branch)
      GIT_BRANCH=$1
      shift
      ;;
    --conda-tag)
      CONDA_TAG=$1
      shift
      ;;
  esac
done

[ -z "${CONDA_TAG}" ] && echo "Missing required --conda-tag" && exit 1

[ -z "${GIT_BRANCH}" ] && echo "Missing required --git-branch" && exit 1

sed -i.tag.bak "s/\(.*version: \).*/\1\"${CONDA_TAG}\"/" conda/meta.yaml

sed -i.branch.bak "s/\(.*git_rev: \).*/\1${GIT_BRANCH}/" conda/meta.yaml

conda build -c conda-forge --output-folder $PWD/_build conda/

if [[ $PUSH -eq 1 ]]
then
  anaconda login

  PACKAGE=$(conda build -c conda-forge --output-folder $PWD/_build --output conda/)

  anaconda upload -u cdat -i $PACKAGE
fi
