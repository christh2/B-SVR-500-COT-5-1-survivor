# Generated by Django 5.1.1 on 2024-09-10 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip',
            name='tip',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='tip',
            name='title',
            field=models.TextField(max_length=500),
        ),
    ]
