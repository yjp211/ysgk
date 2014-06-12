# -*- coding:utf-8 -*-
from django.shortcuts import render, HttpResponse

from src.models import Tag, Game

from src.misc.base.view import require_post
from src.misc.base.view import BaseView

from src.app.game.service import game_service

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
    def add(self, request):
        """
        添加游戏
        """
        game = Game()
        game.name = request.POST.get('name')       # 英文名称
        game.name_ch = request.POST.get('name_ch')     # 中文名称

        game.desc = request.POST.get('desc')                        # 描述（英文）
        game.desc_ch = request.POST.get('desc_ch')                     # 描述（中文）
        game.tag_ids = request.POST.get('tags')          # 标签_ids
        game.icon_id = int(request.POST.get('icon'))          # 图标文件_id
        game.screen_ids = request.POST.get('screens')          # 截图文件_ids
        game.rec_screen_id = request.POST.get('rec_screen')          # 推荐图片_id
        game.flash_id = request.POST.get('flash')          # flash文件_id
        game.apk_id = request.POST.get('apk')          # apk文件_id
        game.ipa_id = request.POST.get('ipa')          # apk文件_id
        game.apk_pack_id = request.POST.get('apk_pack')         # 本地应用商店打包文件

        ret =  game_service.add_game(game)
        return HttpResponse(ret.to_json())

    def list(self, request, template='game/game_list.html'):
        """
        展示所有游戏
        """
        game_list = Game.objects.all()
        return render(request, template, locals())


game_views = Views()