# Generated by Django 5.0.3 on 2024-07-18 17:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userguide_pass_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_adress', models.GenericIPAddressField(verbose_name='IP адрес')),
                ('setup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='views', to='user.userguide')),
            ],
            options={
                'verbose_name': 'Просмотр',
                'verbose_name_plural': 'Просмотры',
            },
        ),
    ]
