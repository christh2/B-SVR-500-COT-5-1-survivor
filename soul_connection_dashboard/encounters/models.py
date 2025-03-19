# Create your models here.
from django.db import models
from customer.models import Customer
from django.core.validators import MaxValueValidator, MinValueValidator

class Encounter(models.Model):
    def __str__(self):
        return f'{self.id} - {self.customer_id} - {self.id}'
    id = models.IntegerField(unique=True, primary_key=True)
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='encounters')
    date = models.CharField(max_length=1000, blank=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField(max_length=500, blank=True)
    source = models.CharField(max_length=500, blank=True)
