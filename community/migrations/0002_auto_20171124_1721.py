# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-24 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='contentType',
        ),
        migrations.AddField(
            model_name='community',
            name='conType',
            field=models.CharField(max_length=100, null=True),
        ),
    ]