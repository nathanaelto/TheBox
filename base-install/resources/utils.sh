#!/bin/bash

set -xe

apt-get update -y
apt-get upgrade -y
apt-get install -y --no-install-recommends apt-transport-https git make build-essential libcap-dev

rm -rf /var/lib/apt/lists/*
