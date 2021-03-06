# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='recruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=128)),
                ('address', models.TextField()),
                ('tel', models.CharField(max_length=14)),
                ('descript', models.TextField()),
                ('status', models.CharField(choices=[('D', '\u7533\u8acb\u4e2d'), ('P', '\u627f\u8a8d'), ('C', '\u5374\u4e0b')], default='D', max_length=1)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
    ]
