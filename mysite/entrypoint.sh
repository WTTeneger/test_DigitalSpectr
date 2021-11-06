#! /bin/bash

python manage.py migrate zero --no-input

python manage.py makemigrations --no-input

python manage.py migrate --no-input

python manage.py collectstatic --no-input

python manage.py shell < createsuperu.py

exec gunicorn mysite.wsgi:application -b 0.0.0.0:8000 --reload

python manage.py migrate --no-input



#python manage.py runserver 0.0.0.0:8000
