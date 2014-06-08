# -*- coding:utf-8 -*-
from django.shortcuts import render

from src.misc.base.view import BaseView

__all__ = ['home_views']

class Views(BaseView):
    """
    主页试图类
    """

    def index(self, request, template='home/index.html'):
        """
        主页
        """
        return render(request, template)


home_views = Views()