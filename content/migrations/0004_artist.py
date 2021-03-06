# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-03 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20170303_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('about', models.TextField()),
                ('life_image', models.ImageField(upload_to='')),
                ('serial_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
