# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class member(models.Model):

    rank_choices = (('00', '名誉会長'), ('01', '会長'), ('02', '部会長'),
                    ('03', '常任理事'), ('04', '監事'))
    accessibility_choices = ((1, '公開'), (2, '会員のみ'), (3, '非公開'))

    accessibility = models.IntegerField(choices=accessibility_choices)
    rank = models.CharField(max_length=2, choices=rank_choices)
    name = models.CharField(max_length=128, null=False)
    popular_name = models.CharField(max_length=128)
    job_title = models.CharField(max_length=128)
    company_name = models.CharField(max_length=128, null=False)
    biz_type = models.CharField(max_length=256, null=True)
    tel = models.CharField(max_length=128, null=True)
    fax = models.CharField(max_length=128, null=True)
    zipcode = models.CharField(max_length=8)
    address = models.CharField(max_length=256, null=True)
    url = models.URLField(max_length=256, null=True)
    image = models.ImageField()
    created_at = models.DateTimeField(
        'created time', auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(
        'updated time', auto_now=True, blank=True, null=True)
