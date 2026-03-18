# Create Custom User
Django has its own `user` class. But if we want to add some custom fields then we have to create a custom user class. **Note that this class has to be created before running our initial migration**.

## Create CustomUser Model
- Create a custom user model `CustomUser` at `app_name/model.py` e.g. `accounts/models.py` file
- Add the `CustomUser` model as default to the `django_rest_framework/settings.py`. 
- Simply add `AUTH_USER_MODEL = 'accounts.CustomUser'` at the project settings.
- Run migration and Start the server

# Run Migration and Start Server
- After creating custom user, now we create our first migration file and run migration
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
- We can run our server using the following command.
```bash
python3 manage.py runserver
```