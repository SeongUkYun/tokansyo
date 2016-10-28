from __future__ import unicode_literals

from django.db import models


class gallery(models.Model):
    image = models.ImageField(upload_to='media/uploads/gallery/')
    name = models.CharField(max_length=128, blank=True, null=True)
    descript = models.CharField(max_length=512, blank=True, null=True)
    event_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(
        'created time', auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(
        'updated time', auto_now=True, blank=True, null=True)
