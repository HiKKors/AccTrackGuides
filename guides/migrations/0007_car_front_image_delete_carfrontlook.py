# Generated by Django 5.0.3 on 2024-07-20 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0006_rename_image_carfrontlook_front_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='front_image',
            field=models.ImageField(blank=True, upload_to='car_front_looks'),
        ),
        migrations.DeleteModel(
            name='CarFrontLook',
        ),
    ]
