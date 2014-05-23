# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from src.app.home.views import home_views

urlpatterns = patterns('',
    url(r'^$', home_views.index, name='home_index'),
)
