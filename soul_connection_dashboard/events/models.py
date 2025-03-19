from django.db import models
from coach.models import Employee


class Event(models.Model):
    def __str__(self):
        return f'{self.id} - {self.name}- {self.date}- {self.duration}'
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=500)
    date = models.CharField(max_length=5000)
    duration = models.IntegerField()
    max_participants = models.IntegerField()
    location_x = models.CharField(max_length=500)
    location_y = models.CharField(max_length=500)
    type = models.CharField(max_length=500)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='encounters')
    location_name = models.CharField(max_length=500)
