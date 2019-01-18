#! /bin/bash

if [[ $# -lt 1 ]]
then
  echo -e "Usage: $0 version"

  exit 1
fi

VERSION=$1

sed -i "s|\(.*version: \).*|\1\"${VERSION}\"|" ./conda/meta.yaml

sed -i "s|\(.*git_rev: \).*|\1${VERSION}|" ./conda/meta.yaml

sed -i "s|\(__version__ = ).*|\1\'${VERSION}\'|" ./cwt/__init__.py

sed -i "s|\(.*jasonb87/cwt_api:\)|\1${VERSION}|" ./docs/source/cwt_docker.md
