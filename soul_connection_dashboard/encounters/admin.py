# Register your models here.
from django.contrib import admin
from .models import Encounter

class EncounterAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_id', 'date')
admin.site.register(Encounter, EncounterAdmin)
