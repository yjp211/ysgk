# -*- coding:utf-8 -*-
from django.shortcuts import render, HttpResponse, Http404

from src.misc.base.view import BaseView

#from src.app.game.service import game_service

__all__ = ['game_views']

class Views(BaseView):
    """
    游戏管理视图
    """

    def index(self, request, template='game/game_index.html'):
        """
        游戏管理界面
        """
        return render(request, template)




game_views = Views()