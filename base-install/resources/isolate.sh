#!/bin/bash

set -xe

git clone https://github.com/ioi/isolate.git /tmp/isolate
cd /tmp/isolate
make install
# rm -rf /tmp/*