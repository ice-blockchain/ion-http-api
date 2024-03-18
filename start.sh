#!/bin/bash

mkdir private
curl -sL https://raw.githubusercontent.com/ice-blockchain/ion-controller/ion-fork/config/ion-testnet-global.config.json > private/ion-testnet-global.config.json

./configure.py

TON_API_TONLIB_LITESERVER_CONFIG=private/ion-testnet-global.config.json docker compose up -d --build
