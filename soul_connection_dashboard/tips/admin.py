# Register your models here.
from django.contrib import admin

from .models import Tip

class TipAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
admin.site.register(Tip, TipAdmin)

