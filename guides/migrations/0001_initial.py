# Generated by Django 5.0.3 on 2024-06-21 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('image', models.ImageField(blank=True, upload_to='cars_imgs')),
            ],
        ),
        migrations.CreateModel(
            name='GuideData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('trackName', models.CharField(max_length=128)),
                ('carName', models.CharField(max_length=128)),
                ('time', models.CharField(max_length=64)),
                ('video_url', models.CharField(max_length=500)),
                ('carSettings', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('image', models.ImageField(blank=True, upload_to='tracks_imgs')),
            ],
        ),
    ]
