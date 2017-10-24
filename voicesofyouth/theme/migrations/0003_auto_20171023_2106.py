# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 21:06
from __future__ import unicode_literals

from django.db import migrations

import voicesofyouth.translation.fields


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0002_auto_20171023_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='description',
            field=voicesofyouth.translation.fields.TextFieldTranslatable(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='name',
            field=voicesofyouth.translation.fields.CharFieldTranslatable(max_length=256, verbose_name='Name'),
        ),
    ]
