# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-21 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photogallery', '0009_auto_20170122_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
