# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 20:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20171009_1912'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectsetting',
            old_name='location',
            new_name='region',
        ),
    ]
