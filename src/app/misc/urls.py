# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from src.app.misc.views import misc_views


urlpatterns = patterns('',

    url(r'^upload_file/$', misc_views.upload_file, name='misc_upload_file'),
    url(r'^delete_file/$', misc_views.delete_file, name='misc_delete_file'),
)
