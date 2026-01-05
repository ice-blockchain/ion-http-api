#!/bin/bash

set -e

echo "Running api with ${ION_API_WEBSERVERS_WORKERS:-1} workers"
echo "ENVIRONMENT:"
printenv

gunicorn -k uvicorn.workers.UvicornWorker -w ${ION_API_WEBSERVERS_WORKERS:-1} --bind 0.0.0.0:${ION_API_HTTP_PORT:-8081} pyTON.main:app
