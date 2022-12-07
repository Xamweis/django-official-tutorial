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

- Shop-Frontend: http://127.0.0.1:8000/
- Admin interface: http://127.0.0.1:8000/admin/ `(User: admin, PW: admin)`

---

## Import / export resource data

https://django-import-export.readthedocs.io/

```shell
# https://django-import-export.readthedocs.io/en/latest/installation.html#installation-and-configuration

pip install django-import-export

python manage.py collectstatic
```

#### Exporting

```shell
# https://django-import-export.readthedocs.io/en/latest/getting_started.html#exporting-data

>>> from polls.admin import ProductResource
>>> dataset = ProductResource().export()
>>> print(dataset.csv)
```

#### Importing

```shell
# https://django-import-export.readthedocs.io/en/latest/getting_started.html#importing-data

>>> import tablib
>>> from import_export import resources
>>> from polls.models import Product
>>>
>>> product_resource = resources.modelresource_factory(model=Product)()
>>>
>>> with open("polls/data/products.csv", "r") as fh: imported_data = tablib.Dataset().load(fh)
>>>
>>> result = product_resource.import_data(imported_data, dry_run=True)
>>> print(result.has_errors())
>>>
>>> result = product_resource.import_data(imported_data, dry_run=False)
```
