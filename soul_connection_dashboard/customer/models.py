from django.db import models
from coach.models import Employee

class Customer(models.Model):
    def __str__(self):
        return f'{self.name}'
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    birth_date = models.CharField(max_length=1000, blank=True)
    gender = models.CharField(max_length=100)
    description = models.TextField(max_length=5000, blank=True)
    astrological_sign = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to='customer_images/')
    coach = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='clients', blank=True)


class Payment(models.Model):
    def __str__(self):
        return f'{self.customer} - {self.date} - {self.amount}'
    id = models.IntegerField(unique=True, primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    date = models.CharField(max_length=1000, blank=True)
    payment_method = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.CharField(max_length=100)

class Clothe(models.Model):
    def __str__(self):
        return f'{self.customer} - {self.id} - {self.type}'
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    id = models.IntegerField(unique=True, primary_key=True)
    type = models.CharField(max_length=200, blank=False)
    image = models.ImageField(upload_to='customer_clothes_images/')