# Create your models here.
from django.db import models
from coach.models import Employee
from customer.models import Customer

class Meeting(models.Model):
    def __str__(self):
        return f'{self.date} - {self.coach} - {self.customer}'
    class Rating(models.IntegerChoices):
        One = 1; Two = 2; Three = 3; Four = 4; Five = 5
    coach = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    rating = models.IntegerField(choices=Rating.choices)
    report = models.TextField(blank=True)
    source = models.CharField(max_length=100)
