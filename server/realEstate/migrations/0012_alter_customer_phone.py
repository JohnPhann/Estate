# Generated by Django 4.2 on 2023-09-19 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realEstate', '0011_customer_birthdate_customer_cmnd_customer_cmnddate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
