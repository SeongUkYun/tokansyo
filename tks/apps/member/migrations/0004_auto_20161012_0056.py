# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_member_auth_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='accessibility',
            field=models.IntegerField(choices=[(1, '\u516c\u958b'), (2, '\u4f1a\u54e1'), (3, '\u975e\u516c\u958b')]),
        ),
    ]
