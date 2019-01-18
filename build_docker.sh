#! /bin/bash

function usage {
  echo -e "Usage: $0 version [--push]"
}

if [[ $# -lt 1 ]]
then
  usage

  exit 1
fi

VERSION=$1

shift

PUSH=0

while [[ $# -gt 0 ]]
do
  ARG=$1

  shift

  case $ARG in
    --push)
      PUSH=1
      ;;
    *)
      usage

      exit 1
      ;;
  esac
done

git checkout ${VERSION}

docker build -t jasonb87/cwt_api:${VERSION} -f docker/Dockerfile .

if [[ $PUSH -eq 1 ]]
then
  docker login

  docker push jasonb87/cwt_api:${VERSION}
fi
