# Create Package
We might want to create different folders which we may want to keep as package. To make a folder as package, we have to create a file `__init__.py`.

In Python, a package is a way of organizing related modules (i.e., .py files) together inside a folder so they can be easily **reused** and **imported** elsewhere.

`__init__.py` is a special Python file that --
- Marks a folder as a package.
- Is executed when the package is imported.
- Can be empty, or include initialization code for the package.

# Create Django Apps
To create an app we need to run the following command 
```bash
django-admin startapp core
```

Next we have to update the app name to the `apps.py` file of the app. 
The app name format is `package_name.app_name`
Example
```py
from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core'
```
Here `apps` is the package name where the app resides and `core` is the app name.

Next we need to include app name into `settings.py` file's `INSTALLED_APPS` array. 