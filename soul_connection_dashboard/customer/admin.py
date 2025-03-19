# Register your models here.
from django.contrib import admin
from .models import Customer, Payment, Clothe

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'email')
admin.site.register(Customer, CustomerAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date')
admin.site.register(Payment, PaymentAdmin)

class ClotheAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'customer')
admin.site.register(Clothe, ClotheAdmin)
