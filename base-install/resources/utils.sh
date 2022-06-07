#!/bin/bash

set -xe

apt-get update -y
apt-get install -y apt-transport-https
apt-get upgrade -y
apt-get install -y git make build-essential libcap-dev curl

# rm -rf /var/lib/apt/lists/*
