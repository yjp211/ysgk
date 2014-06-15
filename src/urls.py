# -*- coding:utf-8 -*-
import os
import mimetypes

from django.conf.urls import patterns, include, url
from django.views.static import serve
from src.settings import PROJECT_ROOT, STATIC_ROOT

mimetypes.knownfiles.append(os.path.join(PROJECT_ROOT, 'mime.type'))


urlpatterns = patterns('src.views',
    url(r'^$', 'home', name='kss_home'),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
)

urlpatterns += patterns('',
    url(r'^api/', include('src.api.urls')),
    url(r'^misc/', include('src.app.misc.urls')),
    url(r'^home/', include('src.app.home.urls')),
    url(r'^auth/', include('src.app.auth.urls')),
    url(r'^game/', include('src.app.game.urls')),
    url(r'^store/', include('src.app.store.urls')),
)
