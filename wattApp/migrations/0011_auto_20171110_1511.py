# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 15:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wattApp', '0010_auto_20171110_1442'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HMesure',
            new_name='HMeasure',
        ),
        migrations.RenameModel(
            old_name='TMesure',
            new_name='TMeasure',
        ),
    ]
