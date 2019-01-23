# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-21 12:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_populate_blogpageauthor_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpageauthor',
            name='author_person_page',
        ),
        migrations.AlterField(
            model_name='blogpageauthor',
            name='author',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='people.Author'),
            preserve_default=False,
        ),
    ]
