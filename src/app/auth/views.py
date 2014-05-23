# -*- coding:utf-8 -*-

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from src.misc.base.view import BaseView, require_post

from src.app.auth.service import auth_service

__all__ = ['auth_views']

class Views(BaseView):
    """
    认证试图
    """

    def index(self, request, template='auth/login.html'):
        """
        进入认证界面
        """
        return render(request, template)


    @require_post
    def login_in(self, request):
        """
        认证用户
        """

        username = request.POST.get('username', '')
        passwd = request.POST.get('passwd', '')

        ret = auth_service.auth_user(username, passwd)

        if ret.success:
            messages.success(request, u'%s认证用户成功' % username)
            return redirect(reverse('home_index'))
        else:
            messages.error(request, u'%s认证用户失败，%s' % (username, ret.msg))
            return redirect(reverse('login_index'))

    def login_out(self, request):
        """
        用户登出
        """
        return redirect(reverse('login_index'))


auth_views = Views()