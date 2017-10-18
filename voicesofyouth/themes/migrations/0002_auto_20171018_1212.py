# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 12:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        ('tags', '0002_auto_20171018_1212'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maps', '0002_auto_20171018_1212'),
        ('themes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='themetags',
            name='created_by',
            field=models.ForeignKey(help_text='The user which originally created this item', on_delete=django.db.models.deletion.CASCADE, related_name='themes_themetags_creations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='themetags',
            name='modified_by',
            field=models.ForeignKey(help_text='The user which last modified this item', on_delete=django.db.models.deletion.CASCADE, related_name='themes_themetags_modifications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='themetags',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tags.Tag'),
        ),
        migrations.AddField(
            model_name='themetags',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theme_tags', to='themes.Theme'),
        ),
        migrations.AddField(
            model_name='themelanguage',
            name='created_by',
            field=models.ForeignKey(help_text='The user which originally created this item', on_delete=django.db.models.deletion.CASCADE, related_name='themes_themelanguage_creations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='themelanguage',
            name='modified_by',
            field=models.ForeignKey(help_text='The user which last modified this item', on_delete=django.db.models.deletion.CASCADE, related_name='themes_themelanguage_modifications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='themelanguage',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theme_language', to='themes.Theme'),
        ),
        migrations.AddField(
            model_name='themefavoriteby',
            name='created_by',
            field=models.ForeignKey(help_text='The user which originally created this item', on_delete=django.db.models.deletion.CASCADE, related_name='themes_themefavoriteby_creations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='themefavoriteby',
            name='modified_by',
            field=models.ForeignKey(help_text='The user which last modified this item', on_delete=django.db.models.deletion.CASCADE, related_name='themes_themefavoriteby_modifications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='themefavoriteby',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='themes.Theme'),
        ),
        migrations.AddField(
            model_name='theme',
            name='created_by',
            field=models.ForeignKey(help_text='The user which originally created this item', on_delete=django.db.models.deletion.CASCADE, related_name='themes_theme_creations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='theme',
            name='map',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='map_themes', to='maps.Map'),
        ),
        migrations.AddField(
            model_name='theme',
            name='mappers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='theme',
            name='modified_by',
            field=models.ForeignKey(help_text='The user which last modified this item', on_delete=django.db.models.deletion.CASCADE, related_name='themes_theme_modifications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='theme',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
    ]
