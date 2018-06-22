#!/bin/sh

#
# set env GITHUB_TOKEN
#

docker run --rm \
  -e DC_OS=$(uname -s) \
  -e DC_MACHINE=$(uname -m) \
  -e GITHUB_TOKEN=${GITHUB_TOKEN} \
  -v /opt:/out \
  -v $(pwd):/tmp \
  -w /tmp \
  python:3 /bin/bash -c \
  "pip install -r requirements.txt && \
   python setup.py"

docker run --rm \
  -v /opt/bin:/out \
  debian /bin/bash -c \
  "apt-get update && \
   apt-get -y install make && \
   cp /usr/bin/make /out/make"

