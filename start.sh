#!/bin/bash

# mkdir private
# curl -sL http://94.100.16.219/configs/global.config.json > private/ion-testnet-global.config.json

./configure.py

TON_API_TONLIB_LITESERVER_CONFIG=private/ion-testnet-global.config.json docker compose up -d --build
