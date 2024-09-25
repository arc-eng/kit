docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
    -i https://arcane.engineer/api/openapi.yaml \
    -g python \
    --additional-properties generateSourceCodeOnly=true,projectName=arcane-engine,packageName=arcane \
    -o /local