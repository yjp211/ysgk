# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url
from src.api.game.views import views

urlpatterns = patterns('',
    url(r'^categories/$', views.get_all_category, name='api_game_get_all_categories'),
    url(r'^category/hot/$', views.list_hot_category, name='api_game_list_hot_category'),
    url(r'^category/(?P<id>.+)/$', views.list_category, name='api_game_list_category'),
    #url(r'^tail/(?P<id>.+)/$', views.tail, name='api_game_tail'),
)

