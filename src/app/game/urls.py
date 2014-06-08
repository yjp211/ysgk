# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from src.app.game.views import game_views


urlpatterns = patterns('',
    url(r'^$', game_views.index, name='game_index'),
    url(r'^list/$', game_views.list, name='game_list'),
    url(r'^prepar_add/$', game_views.prepar_add, name='game_prepar_add'),
    url(r'^add/$', game_views.add, name='game_add'),
)
