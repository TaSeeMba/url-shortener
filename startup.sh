#!/bin/sh
python manage.py migrate --noinput
python manage.py runserver 0.0.0.0:80

# Template gunicorn command if running server behind gunicorn
#gunicorn --bind :80 --workers 2 mms.wsgi:application