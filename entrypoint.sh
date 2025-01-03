#!/bin/sh

cd "$(dirname "$0")"

if [ -f ".env" ]; then
    source .env
fi


python manage.py migrate
python manage.py initapp

gunicorn --workers 2 --bind 0.0.0.0:5000 edgarui.wsgi:application
