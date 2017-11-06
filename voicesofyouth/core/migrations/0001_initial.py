# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 18:54
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.models import Group
from voicesofyouth.user.models import User

from ..models import PROTECTED_GROUPS


__author__ = 'Elton Pereira'
__email__ = 'eltonplima AT gmail DOT com'
__status__ = 'Development'


def create_protected_groups(apps, schema_editor):
    groups = [Group(name=group) for group in PROTECTED_GROUPS]
    db_alias = schema_editor.connection.alias
    Group.objects.using(db_alias).bulk_create(groups)

def create_super_user(apps, schema_editor):
    User.objects.create_superuser('admin', 'fake@email.com', 'Un1c3f@@')


def create_guest_user(apps, schema_editor):
    User.objects.create_user('guest', first_name='Guest', is_active=False)


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_protected_groups),
        migrations.RunPython(create_super_user),
        migrations.RunPython(create_guest_user)
    ]

