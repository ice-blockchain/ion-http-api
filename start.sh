#!/bin/bash

mkdir private

# v.1.0
# curl -sL https://raw.githubusercontent.com/ice-blockchain/ion-controller/ion-fork/config/ion-testnet-global.config.json > private/ion-testnet-global.config.json

# v.2.0
cp /usr/bin/ion/global.config.json private/ion-testnet-global.config.json

./configure.py

TON_API_TONLIB_LITESERVER_CONFIG=private/ion-testnet-global.config.json docker compose up -d --build
