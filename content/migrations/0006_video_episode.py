# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-03 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20170303_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='episode',
            field=models.IntegerField(default=0),
        ),
    ]
