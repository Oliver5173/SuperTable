# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-29 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.TextField()),
                ('semester', models.TextField()),
                ('searchContent', models.TextField()),
            ],
        ),
    ]