# coding: utf-8
from __future__ import unicode_literals

from django.conf.urls import url
from . import views as view

urlpatterns = [
    url("^$", view.GalleryListView.as_view(), name="photo_list"),
    url("^(?P<pk>\d+)/", view.GalleryView.as_view(), name="photo_detail"),
]
