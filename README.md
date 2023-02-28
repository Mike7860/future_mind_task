The application allows to upload pictures with posibility of resizing them, changing image titles and storing changed images in local filesystem (/uploads directory). The application shows general list of stored files and detailed view by id with url etc. It is develop version of application - do not use them on production.

Repository details:

Dev environment - virtualenv
requirements.txt file prepared -> please use command "python -m pip install -r requirements.txt" in created env
Python - 3.9.1
Framework - Django 4.1.6 (DRF 3.14.0)
Database - PostgreSQL
Storage - filesystem ("/uploads" folder)
Tests - pytest
API Documentation - OpenAPIv3 (swagger)
Dev documentation - readme.md

Endpoints:
POST /images
GET /images
GET /images/:id
