# Generated by Django 4.2 on 2023-09-02 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realEstate', '0009_alter_host_mahost'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phoneNDD',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='representativeName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
