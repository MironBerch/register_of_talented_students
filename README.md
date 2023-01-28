# Foodgram-App [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
create at 28.01.23
## Technology stack:
Python 3, Django 4, openpyxl
## Steps to be followed for first time use
- Run this command - it download requirements
```
pip install -r requirements.txt
```
- Run these commands - they create database
```
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
```
- Run this command - it create superuser
```
python manage.py createsuperuser
```
- Everything is done - now you can start the server
```
python manage.py runserver
```