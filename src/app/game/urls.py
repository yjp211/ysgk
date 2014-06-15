# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from src.app.game.views.game import game_views


urlpatterns = patterns('',
    url(r'^$', game_views.list, name='game_index'),
    url(r'^list/$', game_views.list, name='game_list'),
    url(r'^prepar_add/$', game_views.prepar_update, name='game_prepar_add'),
    url(r'^prepar_update/(?P<id>.+)/$', game_views.prepar_update, name='game_prepar_update'),
    url(r'^update/$', game_views.update, name='game_update'),
    url(r'^tail/(?P<id>.+)/$', game_views.tail, name='game_tail'),
)
