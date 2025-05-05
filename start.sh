#!/bin/bash

mkdir private
curl -sL https://cdn.ice.io/mainnet/global.config.json > private/mainnet.json

./configure.py

docker compose up -d --build
