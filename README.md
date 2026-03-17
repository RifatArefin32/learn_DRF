# Learn Django REST Framework
## How to clone and setup the project
Clone the repository first
```bash
git clone git@github.com:RifatArefin32/learn_DRF.git
```
Create and activate a virtual environment
```bash
python3 -m venv env
source env/bin/activate
```
Install the libraries from the `requirements.txt` file
```bash
pip install -r requirements.txt
```
Now, enter into the postgres database and create a database, a user and then grant the user to that database
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

## Important Notes
- [Project Setup](/notes/01_project_setup.md)
- [Create Package and Django App](/notes/02_create_package_and_app.md)

## References
- [Django REST Framework - BugBytes](https://www.youtube.com/watch?v=6AEvlNgRPNc&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=2)
- [Django REST Framework Documentation](https://www.django-rest-framework.org/)