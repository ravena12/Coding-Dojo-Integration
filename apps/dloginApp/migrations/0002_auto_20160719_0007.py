# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 00:07
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('dloginApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Email',
            new_name='User',
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('userManager', django.db.models.manager.Manager()),
            ],
        ),
    ]