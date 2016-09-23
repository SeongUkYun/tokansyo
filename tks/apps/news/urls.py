# coding: utf-8
from __future__ import unicode_literals

from django.conf.urls import url
from . import views as view

urlpatterns = [
    url("^tokan/$", view.TokanNewsListView.as_view(), name="tokannews_list"),
    url("^tokan/(?P<pk>\d+)/", view.TokanNewsView.as_view(), name="tokannews_detail"),
    url("^tax/$", view.TokanNewsListView.as_view(), name="tokannews_list"),
    url("^tax/(?P<pk>\d+)/", view.TokanNewsView.as_view(), name="tokannews_detail"),
    url("^week/$", view.TokanNewsListView.as_view(), name="tokannews_list"),
    url("^week/(?P<pk>\d+)/", view.TokanNewsView.as_view(), name="tokannews_detail"),
]
