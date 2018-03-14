# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-30 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_auto_20171130_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cName', models.CharField(max_length=100)),
                ('tName', models.CharField(max_length=100)),
                ('conType', models.CharField(max_length=100, null=True)),
                ('content', models.TextField()),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]