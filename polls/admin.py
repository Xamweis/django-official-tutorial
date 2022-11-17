from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Product, Customer, Order


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product


class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer


class OrderResource(resources.ModelResource):
    class Meta:
        model = Order


class ProductAdmin(ImportExportModelAdmin):
    resource_classes = [ProductResource]


class CustomerAdmin(ImportExportModelAdmin):
    resource_classes = [CustomerResource]


class OrderAdmin(ImportExportModelAdmin):
    resource_classes = [OrderResource]


admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
