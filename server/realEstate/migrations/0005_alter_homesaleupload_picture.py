# Generated by Django 4.2 on 2023-09-01 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realEstate', '0004_rename_images_homesale_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homesaleupload',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m'),
        ),
    ]
