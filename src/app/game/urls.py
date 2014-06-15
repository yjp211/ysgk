# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from src.app.game.views.game import game_views
from src.app.game.views.tag import tag_views
from src.app.game.views.category import category_views


urlpatterns = patterns('',
    url(r'^$', game_views.list, name='game_index'),
    url(r'^list/$', game_views.list, name='game_list'),
    url(r'^prepar_add/$', game_views.prepar_update, name='game_prepar_add'),
    url(r'^prepar_update/(?P<id>.+)/$', game_views.prepar_update, name='game_prepar_update'),
    url(r'^update/$', game_views.update, name='game_update'),
    url(r'^delete/(?P<id>.+)/$', game_views.delete, name='game_delete'),
)

urlpatterns += patterns('',

    url(r'^tag/prepar_add/$', tag_views.prepar_update, name='game_tag_prepar_add'),
    url(r'^tag/prepar_update/(?P<id>.+)/$', tag_views.prepar_update, name='game_tag_prepar_update'),
    url(r'^tag/update/$', tag_views.update, name='game_tag_update'),
)

urlpatterns += patterns('',
    url(r'^category/prepar_add/$', category_views.prepar_update, name='game_category_prepar_add'),
    url(r'^category/prepar_update/(?P<id>.+)/$', category_views.prepar_update, name='game_category_prepar_update'),
    url(r'^category/update/$', category_views.update, name='game_category_update'),
)
