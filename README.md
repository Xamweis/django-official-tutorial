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

### Import / export resource data

https://django-import-export.readthedocs.io/

#### Exporting

```shell
# https://django-import-export.readthedocs.io/en/latest/getting_started.html#exporting-data

>>> from polls.admin import ProductResource
>>> dataset = ProductResource().export()
>>> print(dataset)
```

#### Importing

```shell
# https://django-import-export.readthedocs.io/en/latest/getting_started.html#exporting-data

>>> import tablib
>>> from import_export import resources
>>> from polls.models import Product
>>>
>>> product_resource = resources.modelresource_factory(model=Product)()
>>>
>>> dataset = tablib.Dataset(['', 'New product', '444.99', 'Description', 'example.jpg'], headers=['id', 'product', 'price', 'description', 'image_src'])
>>>
>>> result = product_resource.import_data(dataset, dry_run=True)
>>> print(result.has_errors())
>>>
>>> result = product_resource.import_data(dataset, dry_run=False)
```
