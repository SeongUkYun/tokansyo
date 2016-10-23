# -*- coding: utf-8 -*- 
from __future__ import unicode_literals

from django.conf.urls import url
from . import views as view

urlpatterns = [
    url("^$", view.MemberListView.as_view(), name="member_list"),
    url("^(?P<pk>\d+)/", view.MemberView.as_view(), name="member_detail"),
    url("^update/$", view.MemberEditView.as_view(), name="member_update"),
    url("^password/$", view.ApplyPasswordView.as_view(), name="password_apply"),
    url("^complete/$", view.MemberCompleteView.as_view(), name="member_complete"),
    url("^apply_complete/$", view.ApplyCompleteView.as_view(), name="password_apply_complete"),
    url("^reset_complete/$", view.ResetCompleteView.as_view(), name="password_reset_complete"),
]
