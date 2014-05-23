# -*- coding:utf-8 -*-
import os
import mimetypes

from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from settings import PROJECT_ROOT

mimetypes.knownfiles.append(os.path.join(PROJECT_ROOT, 'mime.type'))


urlpatterns = patterns('src.views',
    url(r'^$', 'home', name='kss_home'),
)

urlpatterns += patterns('',
    url(r'^home/', include('src.app.home.urls')),
    url(r'^auth/', include('src.app.auth.urls')),
    url(r'^game/', include('src.app.game.urls')),
)

urlpatterns += staticfiles_urlpatterns()
