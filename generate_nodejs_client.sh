docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
    -i https://arcane.engineer/api/openapi.yaml \
    -g nodejs-express-server \
    --additional-properties generateSourceCodeOnly=true,projectName=arcane-engine \
    -o /local