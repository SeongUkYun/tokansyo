# coding: utf-8
from __future__ import unicode_literals

from django.conf.urls import url
from . import views as view

urlpatterns = [
    url("^$", view.MemberListView.as_view(), name="member_list"),
    url("^(?P<pk>\d+)/", view.MemberView.as_view(), name="member_detail"),
]
