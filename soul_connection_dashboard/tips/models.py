from django.db import models

# Create your models here.

class Tip(models.Model):
    def __str__(self):
        return f'{self.id} - {self.title}'
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.TextField(max_length=500)
    tip = models.TextField(max_length=5000)
