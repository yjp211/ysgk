# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from src.app.store.views import store_views



urlpatterns = patterns('',
    url(r'^$', store_views.list, name='store_index'),
    url(r'^list/$', store_views.list, name='store_list'),
)
