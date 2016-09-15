# coding: utf-8
from __future__ import unicode_literals

from django.conf.urls import url
from . import views as view

urlpatterns = [
    url("^$", view.CalendarListView.as_view(), name="task_list"),
    url("^(?P<pk>\d+)/", view.CalendarTaskView.as_view(), name="task_detail"),
]
