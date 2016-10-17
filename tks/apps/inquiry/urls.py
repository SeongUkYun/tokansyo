# -*- coding: utf-8 -*- 
from __future__ import unicode_literals

from django.conf.urls import url
from . import views as view

urlpatterns = [
    url("^$", view.InquiryView.as_view(), name="inquiry_post"),
    url("^complete/$", view.InquiryCompleteView.as_view(), name="inquiry_complete"),
]
