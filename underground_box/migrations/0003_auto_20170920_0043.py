# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-20 00:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('underground_box', '0002_auto_20170916_2326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='undergroundbox',
            name='box_id',
        ),
        migrations.RemoveField(
            model_name='undergroundboxtype',
            name='type_id',
        ),
    ]