# coding: utf-8
from __future__ import unicode_literals

from django.conf.urls import url
from . import views as view

urlpatterns = [
    url("^tokan/$", view.TokanNewsListView.as_view(), name="tokannews_list"),
    url("^tokan/(?P<pk>\d+)/", view.TokanNewsView.as_view(), name="tokannews_detail"),
    url("^tax/$", view.TaxNewsListView.as_view(), name="taxnews_list"),
    url("^tax/(?P<pk>\d+)/", view.TaxNewsView.as_view(), name="taxnews_detail"),
    url("^week/$", view.WeekNewsListView.as_view(), name="weeknews_list"),
    url("^week/(?P<pk>\d+)/", view.WeekNewsView.as_view(), name="weeknews_detail"),
]
