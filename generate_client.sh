#!/bin/bash

# This script generates a Python client from the OpenAPI specification.
# It uses the openapitools/openapi-generator-cli Docker image to perform the generation.

# Exit immediately if a command exits with a non-zero status.
set -e

# Define the OpenAPI specification URL
OPENAPI_SPEC_URL="https://arcane.engineer/api/openapi.yaml"

# Define the output directory
OUTPUT_DIR="/local"

# Run the OpenAPI Generator CLI Docker container
# - --rm: Automatically remove the container when it exits
# - -v "${PWD}:/local": Bind mount the current directory to /local in the container
# - -i: Input OpenAPI specification URL
# - -g: Generator name (python)
# - --additional-properties: Additional properties for the generator
# - -o: Output directory

docker run --rm -v "${PWD}:${OUTPUT_DIR}" openapitools/openapi-generator-cli generate \
    -i ${OPENAPI_SPEC_URL} \
    -g python \
    --additional-properties generateSourceCodeOnly=true,projectName=arcane-engine,packageName=arcane \
    -o ${OUTPUT_DIR}
