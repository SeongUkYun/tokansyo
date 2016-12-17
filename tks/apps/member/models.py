# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class member(models.Model):

    header = ['公開範囲',
              '職位',
              '姓名',
              '通称名',
              '役職',
              '会社名',
              '業種',
              '会社TEL',
              '会社FAX',
              '郵便番号',
              '会社住所',
              '携帯番号']

    rank_choices = (('90', '常任顧問'), ('91', '顧問'), ('92', '相談役'),
                    ('93', '参与'), ('00', '名誉会長'), ('01', '会長'), ('02', '副会長'),
                    ('10', '常任理事'), ('12', '理事'), ('19', '会員'),
                    ('11', '監事'), ('95', '諮問委員'), ('99', 'サイト管理者'))
    accessibility_choices = ((1, '公開'), (2, '会員のみ'), (3, '非公開'))

    auth_user = models.ForeignKey('auth.User', null=True, blank=True, related_name='member')
    accessibility = models.IntegerField(choices=accessibility_choices)
    rank = models.CharField(max_length=2, choices=rank_choices)
    name = models.CharField(max_length=128, null=False)
    popular_name = models.CharField(max_length=128, blank=True, null=True)
    job_title = models.CharField(max_length=128)
    company_name = models.CharField(max_length=128, null=False)
    biz_type = models.CharField(max_length=256, null=True)
    tel = models.CharField(max_length=128, null=True)
    fax = models.CharField(max_length=128, null=True)
    zipcode = models.CharField(max_length=8)
    address = models.CharField(max_length=256, null=True)
    email = models.EmailField(null=True, blank=True)
    url = models.URLField(max_length=256, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    init_entry = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        'created time', auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(
        'updated time', auto_now=True, blank=True, null=True)

    def parsedName(self):
        return self.name.split(' ')

    def first_name(self):
        return self.name.split(' ')[1]

    def last_name(self):
        return self.name.split(' ')[0]

    @property
    def display_rank(self):
        return dict((x, y) for x, y in self.rank_choices)[self.rank]

    @property
    def display_level(self):
        return dict((x, y) for x, y in self.accessibility)[self.accessibility]
