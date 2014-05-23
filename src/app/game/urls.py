# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from src.app.game.views import game_views

urlpatterns = patterns('',
    url(r'^$', game_views.index, name='game_index'),

)
