# Register your models here.
from django.contrib import admin
from .models import Employee, Message

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'email')
admin.site.register(Employee, EmployeeAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver')
admin.site.register(Message, MessageAdmin)
