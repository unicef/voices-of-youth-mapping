# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 13:51
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('medias', '0006_remove_media_enabled'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='media',
            options={'default_manager_name': 'default_objects'},
        ),
        migrations.AlterModelManagers(
            name='media',
            managers=[
                ('default_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
