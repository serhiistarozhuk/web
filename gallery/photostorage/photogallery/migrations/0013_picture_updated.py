# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-21 23:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photogallery', '0012_auto_20170722_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]