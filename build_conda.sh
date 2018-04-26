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
  esac
done

conda build -c conda-forge --output-folder $PWD/_build conda/

if [[ $PUSH -eq 1 ]]
then
  anaconda login

  PACKAGE=$(conda build -c conda-forge --output conda/)

  anaconda upload -c uvcdat -i --force $PACKAGE
fi
