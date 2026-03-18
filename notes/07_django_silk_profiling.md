# Django Silk 

## Key Features of Django Silk
### SQL Profiling
- Captures and shows all SQL queries per request.
- Highlights duplicate queries (N+1 issues).
- Displays execution time and raw SQL.
### Request/Response Profiling
- Tracks the time taken for each HTTP request.
- Provides detailed breakdowns of middleware and view processing times.
### Code Profiling
- Can perform Python function-level profiling using `cProfile`.
- We can mark custom functions with @silk_profile to analyze them.
### UI Dashboard
- A built-in admin-style interface available at /silk/.

## Installation
Run command
```bash
pip install django-silk
```
In settings.py add the following:
```py
MIDDLEWARE = [
    ...
    'silk.middleware.SilkyMiddleware',
    ...
]

INSTALLED_APPS = (
    ...
    'silk'
)
```
To enable access to the user interface add the following to `urls.py`:
```py
urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
```
Now run migration.
```bash
python manage.py migrate
```
Silk will automatically begin interception of requests and we can proceed to add profiling if required. The UI can be reached at `/silk/`

Learn more on [Github link](https://github.com/jazzband/django-silk) to install.