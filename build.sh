#! /bin/sh

buildctl-daemonless.sh \
  build \
  --frontend dockerfile.v0 \
  --local context=. \
  --local dockerfile=. \
  $@
