# Generated by Django 5.1.1 on 2024-09-04 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_alter_payments_payment_method'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Payments',
            new_name='Payment',
        ),
    ]
