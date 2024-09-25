docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
    -i https://arcane.engine/api/openapi.yaml \
    -g python \
    --additional-properties generateSourceCodeOnly=true,projectName=pr-pilot,packageName=pr_pilot \
    -o /local