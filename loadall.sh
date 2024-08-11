#!/bin/sh

if [ -n "$WINDIR" ]; then
    # This environment variable is typically present on Windows
    
    echo "Loading data from dump (OS = WINDOWS)"

    py manage.py loaddata dump/all.json

elif [ "$(uname)" = "Darwin" ]; then
    # macOS

    echo "Loading data from dump (OS = MACOS)"

    python manage.py loaddata dump/all.json
    
elif [ "$(uname)" = "Linux" ]; then
    # Linux

    echo "Loading data from dump (OS = LINUX)"

    python manage.py loaddata dump/all.json


else
    echo "Unknown OS"
fi
