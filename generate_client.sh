#!/bin/bash

# Function to handle errors
echo_error() {
    echo "Error: $1" >&2
}

# Check if Docker is installed
docker --version >/dev/null 2>&1 || { echo_error "Docker is not installed. Please install Docker and try again."; exit 1; }

# Run the OpenAPI Generator
if ! docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
    -i https://arcane.engineer/api/openapi.yaml \
    -g python \
    --additional-properties generateSourceCodeOnly=true,projectName=arcane-engine,packageName=arcane \
    -o /local; then
    echo_error "Failed to generate client code. Please check the OpenAPI specification and try again."
    exit 1
fi

# Success message
echo "Client code generated successfully."
