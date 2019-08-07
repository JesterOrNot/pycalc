#! /bin/bash
apt-get update && apt upgrade -y --force-yes \
apt-get install -y apt-utils
apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*
yarn install