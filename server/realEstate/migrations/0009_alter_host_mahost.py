# Generated by Django 4.2 on 2023-09-02 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realEstate', '0008_alter_customer_makh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='mahost',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
