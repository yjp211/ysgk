# -*- coding:utf-8 -*-
import json

from django.shortcuts import render, redirect, HttpResponse
from misc.base.view import require_post

from src.misc.base.view import BaseView
from src.app.game.service import game_service

from src.models import Tag, Game, File

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

    def prepar_add(self, request, template='game/game_add.html'):
        """
        进入添加游戏界面
        """
        tag_list = Tag.objects.all()

        return render(request, template, locals())

    @require_post
    def upload_file(self, request):
        """
        上传文件
        """
        request.FILES
        psot_file = request.FILES.get('file')

        file = File()
        file.name = psot_file.name
        file.size = psot_file.size
        file.url = 'aaaaa'
        print file.save()
        print file.id

        return HttpResponse(json.dumps(file.id))

    @require_post
    def add(self, request, template='game/game_add.html'):
        """
        添加游戏
        """
        game = Game()
        game.name = request.POST.get('name')       # 英文名称
        game.name_ch = request.POST.get('name_ch')     # 中文名称

        game.desc = request.POST.get('desc')                        # 描述（英文）
        game.desc_ch = request.POST.get('desc_ch')                     # 描述（中文）


        return redirect('/game/prepar_add')

    def list(self, request, template='game/game_list.html'):
        """
        展示所有游戏
        """
        game_list = Game.objects.all()
        return render(request, template, locals())




game_views = Views()