# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class news(models.Model):

    NEWS_TYPES = (('N', '韓商ニュース'),
                  ('T', '税経クラブ'),
                  ('W', '週間動向'))

    news_type = models.CharField(max_length=1, choices=NEWS_TYPES)
    title = models.CharField(max_length=128, null=False)
    descript = models.TextField()
    image = models.ImageField(upload_to='media/uploads/news/', blank=True)
    news_file = models.FileField(upload_to='media/uploads/news/')
