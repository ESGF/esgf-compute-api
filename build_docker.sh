#! /bin/bash

function usage {
  echo -e "Usage: $0 git_branch docker_tag [--push]"
}

if [[ $# -lt 2 ]]
then
  usage

  exit 1
fi

BRANCH=$1

shift

TAG=$1

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

docker build -t jasonb87/cwt_api:$TAG --build-arg BRANCH=$BRANCH docker/

if [[ $PUSH -eq 1 ]]
then
  docker login

  docker push jasonb87/cwt_api:$TAG
fi
