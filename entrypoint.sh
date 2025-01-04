#!/bin/sh

cd "$(dirname "$0")"

if [ -f "/secrets/app_config" ]; then
    source /secrets/app_config
    echo "App config loaded"
else
    echo "App config not found, use defaults"
fi

python manage.py collectstatic --no-input > /dev/null
python manage.py migrate > /dev/null
python manage.py initapp

gunicorn --workers 2 --bind 0.0.0.0:8000 edgarui.wsgi:application
