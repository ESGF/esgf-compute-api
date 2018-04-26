#! /bin/bash

SED_FLAGS=-i.bak

if [[ $# -eq 1 ]]
then
  echo -e "Usage: $0 version git_tag"

  exit 1
fi

VERSION=$1

TAG=$2

sed $SED_FLAGS "s|\(.*version: \"\).*|\1$VERSION\"|" ./conda/meta.yaml

sed $SED_FLAGS "s|\(.*git_rev: \).*|\1$TAG|" ./conda/meta.yaml
