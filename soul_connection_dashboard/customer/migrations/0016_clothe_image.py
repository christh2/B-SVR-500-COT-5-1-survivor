# Generated by Django 5.1.1 on 2024-09-09 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0015_rename_adress_customer_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothe',
            name='image',
            field=models.ImageField(default='', upload_to='customer_clothes_images/'),
            preserve_default=False,
        ),
    ]
