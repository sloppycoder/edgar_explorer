#!/bin/sh

cd "$(dirname "$0")"

python manage.py collectstatic --no-input > /dev/null
python manage.py migrate > /dev/null
python manage.py initapp

gunicorn --workers 2 --bind 0.0.0.0:8000 edgarui.wsgi:application
