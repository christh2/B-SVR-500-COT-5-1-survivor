# Register your models here.
from django.contrib import admin

from .models import Event
class EnventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'employee')
admin.site.register(Event, EnventAdmin)

