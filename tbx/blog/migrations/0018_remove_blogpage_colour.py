# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-22 15:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_map_tags_to_related_services'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='colour',
        ),
    ]
