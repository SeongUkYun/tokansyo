# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class recruit(models.Model):

    STATUS_TYPES = (('D', '申請中'), ('P', '承認'), ('C', '却下'))

    company_name = models.CharField(max_length=128, null=False)
    address = models.TextField(null=False)
    tel = models.CharField(max_length=14, null=False)
    descript = models.TextField()
    status = models.CharField(max_length=1, default='D', choices=STATUS_TYPES)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
