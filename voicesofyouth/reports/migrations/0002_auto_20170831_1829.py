# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 18:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reportfavoriteby',
            options={'verbose_name': 'Reports Favorite By', 'verbose_name_plural': 'Reports Favorite By'},
        ),
        migrations.AlterModelOptions(
            name='reportlanguage',
            options={'verbose_name': 'Reports Languages', 'verbose_name_plural': 'Reports Languages'},
        ),
        migrations.AlterModelOptions(
            name='reporttags',
            options={'verbose_name': 'Reports Tags', 'verbose_name_plural': 'Reports Tags'},
        ),
    ]
