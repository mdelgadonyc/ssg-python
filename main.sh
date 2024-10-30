#!/bin/sh

python3 src/main.py
if [ $? -eq 0 ]; then
    cd public && python3 -m http.server 8888
else
    echo "main.py failed with exit code $?."
fi

