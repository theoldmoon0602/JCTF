# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-25 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0003_auto_20160225_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='hint',
            name='name',
            field=models.CharField(default='', max_length=128),
        ),
    ]