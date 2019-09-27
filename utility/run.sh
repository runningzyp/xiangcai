#!/bin/bash

python manage.py collectstatic --noinput
gunicorn apps.wsgi -w 4 -t 60 --bind 0.0.0.0:5000 --chdir $PWD