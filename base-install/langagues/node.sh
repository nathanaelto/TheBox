#!/bin/bash

set -xe

curl -s https://deb.nodesource.com/setup_16.x | bash

apt-get install nodejs -y

npm install jest --location=global
