# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class recruit(models.Model):

    EMPLOYMENT_TYPES = ((10, '正社員'), (20, '契約社員'), (30, 'パートタイム'))

    member = models.ForeignKey('member.member', on_delete=models.CASCADE, related_name='company')
    work_type = models.CharField(max_length=256)
    work_descript = models.TextField()
    condition = models.TextField()
    employment_type = models.IntegerField(choices=EMPLOYMENT_TYPES)
    contact_to = models.CharField(max_length=128)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
