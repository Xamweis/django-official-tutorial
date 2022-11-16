from datetime import datetime

from django.db import models
from django.utils import timezone


class Products(models.Model):
    # id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    description = models.TextField(blank=True, null=True)


class Customer(models.Model):
    # id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100, blank=False)
    lastName = models.CharField(max_length=100, blank=False)
    street = models.CharField(max_length=100, blank=False)
    plz = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)


class Orders(models.Model):
    # id = models.AutoField(primary_key=True)
    orderDate = models.DateTimeField(default=datetime.now)
    articleOrdered = models.ForeignKey(Products, on_delete=models.CASCADE)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.IntegerField()


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
