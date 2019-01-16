# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-28 09:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('torchbox', '0101_auto_20180912_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='workpage',
            name='feed_image',
            field=models.ForeignKey(blank=True, help_text='Image used on listings and social media.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='torchbox.TorchboxImage'),
        ),
    ]