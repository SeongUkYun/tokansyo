# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-05 03:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0012_auto_20161213_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]