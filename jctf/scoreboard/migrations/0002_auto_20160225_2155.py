# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-25 21:55
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('text', models.TextField()),
                ('url', models.TextField(validators=[django.core.validators.URLValidator()])),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=140, unique=True),
        ),
        migrations.AddField(
            model_name='problem',
            name='solvedby',
            field=models.ManyToManyField(to='scoreboard.User'),
        ),
        migrations.AddField(
            model_name='hint',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoreboard.Problem'),
        ),
    ]