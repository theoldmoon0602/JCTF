# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-25 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0002_auto_20160225_2155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hint',
            name='problem',
        ),
        migrations.AddField(
            model_name='hint',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='problem',
            name='hint',
            field=models.ManyToManyField(to='scoreboard.Hint'),
        ),
    ]
