# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 17:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0009_auto_20171023_1454'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='theme',
            options={'ordering': ('name',)},
        ),
    ]
