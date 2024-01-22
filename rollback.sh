#!/bin/bash

cp -r portfolio portfolio-save
rm -rf portfolio
cp -r ./backups/portfolio-backup portfolio
systemctl restart gunicorn
