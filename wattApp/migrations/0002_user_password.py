# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wattApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=None, max_length=40),
            preserve_default=False,
        ),
    ]