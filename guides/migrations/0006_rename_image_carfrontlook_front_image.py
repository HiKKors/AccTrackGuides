# Generated by Django 5.0.3 on 2024-07-20 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0005_carfrontlook'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carfrontlook',
            old_name='image',
            new_name='front_image',
        ),
    ]
