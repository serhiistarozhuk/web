# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 05:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogallery', '0002_auto_20170122_0348'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='comments',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comments_article',
            new_name='comment_pic',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comments_text',
            new_name='comment_text',
        ),
    ]
