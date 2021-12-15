from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DateTimeField

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)


class Address(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()

# will I need to add a tax field?


class Invoice(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(auto_now=False)
    subtotal = models.DecimalField(max_digits=20, decimal_places=2)
    total = models.DecimalField(max_digits=20, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=20, decimal_places=2)
    balance_due = models.DecimalField(max_digits=20, decimal_places=2)
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, null=True, blank=True)


class billedItem(models.Model):
    description = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.DecimalField(max_digits=20, decimal_places=2)
    total_price = models.DecimalField(max_digits=20, decimal_places=2)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)


class Note(models.Model):
    description = models.CharField(max_length=255)
    billed_item = models.ForeignKey(
        billedItem, on_delete=models.CASCADE, null=True, blank=True)
