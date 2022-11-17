from django.contrib import admin
from import_export import resources

from .models import Product, Customer, Order

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product


class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer


class OrderResource(resources.ModelResource):
    class Meta:
        model = Order
