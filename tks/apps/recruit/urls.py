# coding: utf-8
from __future__ import unicode_literals

from django.conf.urls import url
from . import views as view

urlpatterns = [
    url("^$", view.RecruitListView.as_view(), name="recruit_list"),
    url("^(?P<pk>\d+)/", view.RecruitView.as_view(), name="recruit_detail"),
    url("^apply/", view.RecruitApplyView.as_view(), name="recruit_apply"),
    url("^apply_complete/", view.RecruitApplyCompleteView.as_view(), name="recruit_apply_complete"),
]
