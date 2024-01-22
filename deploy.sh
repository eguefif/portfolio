#!/bin/bash

mv ../backups/portfolio-backup ../backups/portfolio-backup$(date +"%FT%T")
cp -r ../portfolio ../backups/portfolio-backup

git pull

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic

systemctl restart gunicorn
