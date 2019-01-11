# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-01-10 16:14
from __future__ import unicode_literals

from django.db import migrations
from django.core.management import call_command
from django.contrib.contenttypes.models import ContentType


def add_permissions_signage(apps, schema_editor):
    call_command('update_geotrek_permissions', verbosity=0)
    UserModel = apps.get_model('auth', 'User')
    GroupModel = apps.get_model('auth', 'Group')
    PermissionModel = apps.get_model('auth', 'Permission')
    ContentTypeModel = apps.get_model("contenttypes", "ContentType")
    type_permissions = ['add', 'change', 'change_geom', 'delete', 'export', 'read', 'publish']

    # List of deleted models (that are not in the app deleted) In lowercase!

    content_type_signage = ContentTypeModel.objects.get(model='signage', app_label='signage')

    for user in UserModel.objects.all():
        for type_perm in type_permissions:
            if user.user_permissions.filter(codename='%s_signage' % type_perm).exists():
                user.user_permissions.add(PermissionModel.objects.get(
                    codename='%s_signage' % type_perm, content_type=content_type_signage))
    for group in GroupModel.objects.all():
        for type_perm in type_permissions:
            if group.permissions.filter(codename='%s_signage' % type_perm).exists():
                group.permissions.add(PermissionModel.objects.get(
                    codename='%s_signage' % type_perm, content_type=content_type_signage))

    type_permissions_type = ['add', 'change', 'delete']
    content_type_signage_type = ContentTypeModel.objects.get(model='signagetype', app_label='signage')

    for user in UserModel.objects.all():
        for type_perm in type_permissions_type:
            if user.user_permissions.filter(codename='%s_infrastructuretype' % type_perm).exists():
                user.user_permissions.add(PermissionModel.objects.get(
                    codename='%s_signagetype' % type_perm, content_type=content_type_signage_type))


class Migration(migrations.Migration):

    dependencies = [
        ('signage', '0002_change_name_signage'),
        ('authent', '0003_auto_20181203_1518'),
        ('infrastructure', '0010_replace_table_name'),
    ]

    operations = [
        migrations.RunPython(add_permissions_signage)
    ]
