# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-12-27 13:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0012_auto_20191227_1326'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issue',
            options={'ordering': ('priority', 'votes')},
        ),
    ]
