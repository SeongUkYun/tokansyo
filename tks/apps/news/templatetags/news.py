# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template import Library
from django.utils import timezone


register = Library()


@register.filter
def display_date(obj):
    if obj.posted_at:
        return obj.posted_at.strftime('%Y/%m/%d')
    else:
        return obj.created_at.strftime('%Y/%m/%d')
