#!/bin/bash

  if [ "$DEBUG"==True ]; then
      python manage.py makemigrations
      python manage.py migrate
      python manage.py create_admin
      python manage.py collectstatic --no-input
      python manage.py load_data
  fi

python manage.py runserver 0.0.0.0:8001