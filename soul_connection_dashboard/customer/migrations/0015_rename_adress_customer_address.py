# Generated by Django 5.1.1 on 2024-09-05 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0014_rename_clothes_clothe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='adress',
            new_name='address',
        ),
    ]
