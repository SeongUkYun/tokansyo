from __future__ import unicode_literals

from django.db import models


class task(models.Model):

    task_date = models.DateField()
    title = models.CharField(max_length=512, null=False)
    locate = models.CharField(max_length=256, null=True)
    content = models.TextField(max_length=2014, null=True)
    created_at = models.DateTimeField(
        'created time', auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(
        'updated time', auto_now=True, blank=True, null=True)
