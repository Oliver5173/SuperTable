# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 00:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0003_auto_20170726_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchresult',
            name='courseExamDate',
            field=models.DateField(default=django.utils.datetime_safe.date.today),
            preserve_default=False,
        ),
    ]
