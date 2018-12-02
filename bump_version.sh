#! /bin/bash

if [[ $# -lt 3 ]]
then
  echo -e "Usage: $0 version git_tag build"

  exit 1
fi

VERSION=$1

TAG=$2

BUILD=$3

sed -i "s|\(.*version: \"\).*|\1$VERSION\"|" ./conda/meta.yaml

sed -i "s|\(.*git_rev: \).*|\1$TAG|" ./conda/meta.yaml

sed -i "s|\(.*number: \).*|\1$BUILD|" ./conda/meta.yaml

sed -i "s|\(__version__ = '\).*\('\)|\1$VERSION\2|" ./cwt/__init__.py
