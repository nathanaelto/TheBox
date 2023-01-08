#!/bin/bash

set -xe

apt-get install -y --no-install-recommends python3 python3-pip

pip3 install uuid \
    python-dotenv \
    typing \
    typing_extensions \
    zipfile36 \
    flask \
    dataclasses_json \
    "Flask[async]" \
    httpx \
    asgiref \
    pytest \
    flask-talisman \
    gunicorn