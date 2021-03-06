# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 15:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wattApp', '0012_auto_20171129_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant_Measure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('humidity', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wattApp.Plant')),
            ],
        ),
        migrations.CreateModel(
            name='User_Measure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.IntegerField()),
                ('humidity', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wattApp.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='hmeasure',
            name='plant',
        ),
        migrations.RemoveField(
            model_name='tmeasure',
            name='user',
        ),
        migrations.DeleteModel(
            name='HMeasure',
        ),
        migrations.DeleteModel(
            name='TMeasure',
        ),
    ]
