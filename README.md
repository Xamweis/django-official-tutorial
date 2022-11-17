# Getting Started

https://docs.djangoproject.com/en/4.1/intro/

## Install Django package

```shell
# https://docs.djangoproject.com/en/4.1/topics/install/

pip install django
```

## Apply database migrations

```shell
# https://docs.djangoproject.com/en/4.1/topics/migrations/

python manage.py migrate
```

## Start development server

```shell
# https://docs.djangoproject.com/en/4.1/ref/django-admin/#runserver

python manage.py runserver
```

### Visit

- Shop-Frontend: http://127.0.0.1:8000/polls/
- Admin interface: http://127.0.0.1:8000/admin/ `(User: admin, PW: admin)`

### Importing / exporting resource data

https://django-import-export.readthedocs.io/

```shell
# https://django-import-export.readthedocs.io/en/latest/getting_started.html#exporting-data

>>> from polls.admin import ProductResource
>>> dataset = ProductResource().export()
>>> print(dataset)
```
