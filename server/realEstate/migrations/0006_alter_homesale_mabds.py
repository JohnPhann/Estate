# Generated by Django 4.2 on 2023-09-01 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realEstate', '0005_alter_homesaleupload_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homesale',
            name='maBDS',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
