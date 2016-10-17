from __future__ import unicode_literals

from django.db import models


class inquiry(models.Model):

    email = models.EmailField()
    title = models.CharField(max_length=512, blank=False, null=False)
    content = models.TextField(max_length=2014, null=False)

    created_at = models.DateTimeField(
        'created time', auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(
        'updated time', auto_now=True, blank=True, null=True)
