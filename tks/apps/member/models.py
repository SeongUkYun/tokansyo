from __future__ import unicode_literals

from django.db import models


class member(models.Model):

    name = models.CharField(max_length=128, null=False)
    biz_type = models.CharField(max_length=256, null=True)
    ceo_name = models.CharField(max_length=128, null=False)
    tel = models.CharField(max_length=14, null=True)
    address = models.CharField(max_length=256, null=True)
    url = models.URLField(max_length=256, null=True)
    image = models.ImageField()
