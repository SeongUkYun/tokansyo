# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-17 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_auto_20161012_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='rank',
            field=models.CharField(choices=[('00', '\u540d\u8a89\u4f1a\u9577'), ('01', '\u4f1a\u9577'), ('02', '\u90e8\u4f1a\u9577'), ('03', '\u5e38\u4efb\u7406\u4e8b'), ('04', '\u76e3\u4e8b'), ('05', '\u7406\u4e8b')], max_length=2),
        ),
    ]
