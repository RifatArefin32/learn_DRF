# Project Setup

## Create Root Project Directory and Setup Git
Create a root directory `learn_DRF/`
```bash
mkdir learn_DRF
cd learn_DRF/
```
Initialize git and default `.gitignore` file for Django
```bash
git init
touch .gitignore
```

## Install Django
First create a virtual environment `env` and activate it.
```bash
python3 -m venv env
source env/bin/activate
```

Install Django and Django REST Framework libraries
```bash
pip install django
pip install djangorestframework
```

Add a `requirements.txt` file
```bash
pip freeze > requirements.txt
```
After adding or installing each library, we need to update the `requirements.txt` files with the above command.

Create a django project at the root directory
```bash
django-admin startproject learn_DRF .
```
Add `'rest_framework'` to the `INSTALLED_APPS` array at the `settings.py` of the project. 

## PostgreSQL Configuration
Install `psycopg2` for PostgreSQL which is the PostgreSQL adapter for Python. Django uses it to connect to PostgreSQL.
```bash
pip install psycopg2
# or 
pip install psycopg2-binary # for linux users
```
Now, create a database, a user and then grant the user to that database
```bash
sudo -u postgres psql # enter into postgresql
```
```sql
CREATE DATABASE learn_drf_db;
CREATE USER learn_drf_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE learn_drf_db TO learn_drf_user;
```

Update Django Settings to Use PostgreSQL in our `django_rest_framework/settings.py`
```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'learn_drf_db',
        'USER': 'learn_drf_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',  # or your database host
        'PORT': '5432',       # default port for PostgreSQL
    }
}
```

Now run the app using the command:

```bash
python3 manage.py runserver
```