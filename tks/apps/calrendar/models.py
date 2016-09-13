from __future__ import unicode_literals

from django.db import models


class task(models.Model):

    task_date = models.DateField()
    title = models.CharField(max_length=512, null=False)
    content = models.CharField(max_length=2014, null=True)
