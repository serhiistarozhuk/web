# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-22 00:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogallery', '0013_picture_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='updated',
        ),
    ]