#!/bin/bash
pipenv shell
python \
  -m grpc_tools.protoc \
  -I ./Service \
  --python_out=./output/py \
  --grpc_python_out=./output/py \
  ./Service/*.proto \
  ./Service/*.proto