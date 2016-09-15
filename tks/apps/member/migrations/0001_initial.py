# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 04:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('biz_type', models.CharField(max_length=256, null=True)),
                ('ceo_name', models.CharField(max_length=128)),
                ('tel', models.CharField(max_length=14, null=True)),
                ('address', models.CharField(max_length=256, null=True)),
                ('url', models.URLField(max_length=256, null=True)),
                ('image', models.ImageField(upload_to=b'')),
            ],
        ),
    ]
