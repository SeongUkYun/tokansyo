# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from mezzanine.core.models import RichText


# class news(models.Model, RichText):
class news(RichText):

    NEWS_TYPES = (('N', '韓商ニュース'),
                  ('T', '税経クラブ'),
                  ('W', '週間動向'))

    news_type = models.CharField(max_length=1, choices=NEWS_TYPES)
    title = models.CharField(max_length=128, null=False)
    descript = models.TextField()
    image = models.ImageField(upload_to='media/uploads/news/', blank=True)
    stream_link = models.URLField(blank=True, null=True)
    news_file = models.FileField(upload_to='media/uploads/news/', blank=True, null=True)
    flag = models.BooleanField('公開可否', default=False)
    posted_at = models.DateTimeField( 'post time', blank=True, null=True)
    created_at = models.DateTimeField(
        'created time', auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(
        'updated time', auto_now=True, blank=True, null=True)
