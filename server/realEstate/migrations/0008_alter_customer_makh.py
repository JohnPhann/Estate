# Generated by Django 4.2 on 2023-09-02 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realEstate', '0007_customer_makh_host_mahost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='makh',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
