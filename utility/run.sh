#!/bin/bash

python manage.py collectstatic --noinput
gunicorn config.wsgi -w 8 -t 60 --bind 0.0.0.0:5000 --chdir $PWD