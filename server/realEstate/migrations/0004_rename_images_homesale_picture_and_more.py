# Generated by Django 4.2 on 2023-09-01 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realEstate', '0003_rename_images_homehire_picture_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homesale',
            old_name='images',
            new_name='picture',
        ),
        migrations.RenameField(
            model_name='homesaleupload',
            old_name='pic',
            new_name='picture',
        ),
        migrations.AlterField(
            model_name='homesaleupload',
            name='homeSale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='realEstate.homesale'),
        ),
    ]