# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-12-27 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0017_auto_20191227_1337'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issue',
            options={'ordering': ('-priority', '-votes')},
        ),
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[('LOW', 1), ('MEDIUM', 2), ('HIGH', 3)], default='LOW', max_length=6),
        ),
    ]