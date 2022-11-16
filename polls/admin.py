from django.contrib import admin
from .models import Question, Product, Customer, Order

admin.site.register(Question)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
