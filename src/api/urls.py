# -*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^config/', 'src.api.views.config', name='api_config'),
    url(r'^game/', include('src.api.game.urls')),
)
