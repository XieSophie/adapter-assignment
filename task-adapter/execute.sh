#!/bin/bash

if [ "$1" == "default" ]; then
    echo "Run processor.py with default configuration on $2"
    python3 processor.py $2

elif [ "$1" == "nscc" ]; then
    echo "Run processor.py with nscc configuration on $2"
    python3 processor.py $2

else
    echo "Unsupported configuration"
    exit 1
fi
