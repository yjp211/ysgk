# -*- coding:utf-8 -*-
from django.shortcuts import render, HttpResponse

from src.misc.base.view import BaseView


__all__ = ['store_views']


class Views(BaseView):
    """
    应用商店管理视图
    """

    def index(self, request, template='store/store_index.html'):
        """
        应用商店管理界面
        """
        return render(request, template)

    def list(self, request, template='store/store_list.html'):
        """
        展示应用商店
        """
        return render(request, template)



store_views = Views()