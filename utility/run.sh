#!/bin/bash

mv utility/base.py /usr/local/lib/python3.8/site-packages/django/db/backends/mysql/base.py
python manage.py collectstatic --noinput
gunicorn apps.wsgi -w 4 -t 60 --bind 0.0.0.0:5000 --chdir $PWD