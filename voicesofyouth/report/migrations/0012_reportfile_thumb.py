# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-23 19:07
from __future__ import unicode_literals

from django.db import migrations, models
import voicesofyouth.report.models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0011_auto_20180125_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportfile',
            name='thumb',
            field=models.FileField(blank=True, upload_to=voicesofyouth.report.models.get_content_file_path, verbose_name='Thumbnail'),
        ),
    ]
