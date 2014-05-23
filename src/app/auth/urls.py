# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from src.app.auth.views import auth_views

urlpatterns = patterns('',
    url(r'^login/$', auth_views.index, name='login_index'),
    url(r'^login/action/$', auth_views.login_in, name='login_action'),
    url(r'^login/login_out/$', auth_views.login_out, name='login_out'),
)
