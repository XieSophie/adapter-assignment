#!/bin/bash

if [ "$1" == "default" ]; then
    echo "Run default configuration"
  apt-get update
  apt-get -y upgrade
  python3 -m pip install --upgrade pip
  python3 -m pip install -r ./requirements.txt
    exit 0

elif [ "$1" == "nscc" ]; then
    echo "Run nscc configuration"
  python3 -m pip install -r ./requirements.txt
    exit 0

else
    echo "Unsupported configuration"
    exit 1
fi
