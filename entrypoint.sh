#!/bin/sh

cd "$(dirname "$0")"

if [ -f ".env" ]; then
    source .env
fi

gunicorn --workers 2 --bind 0.0.0.0 app:app
