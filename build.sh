#! /bin/sh

buildctl-daemonless.sh \
  build \
  --frontend dockerfile.v0 \
  --local context=. \
  --local dockerfile=. \
  --opt build-arg:CONDA_TOKEN=${CONDA_TOKEN}
