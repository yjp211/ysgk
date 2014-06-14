# -*- coding:utf-8 -*-
from django.shortcuts import render, HttpResponse

from src.models import Tag, Game, Category

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

    def prepar_update(self, request, id='', template='game/game_update.html'):
        """
        进入游戏编辑界面
        """
        if id:
            game = Game.objects.get(id=id)
        tag_list = Tag.objects.all()

        return render(request, template, locals())

    @require_post
    def update(self, request):
        """
        添加游戏
        """
        game = Game()
        game.id = request.POST.get('id', None)       # 英文名称
        game.name = request.POST.get('name')       # 英文名称
        game.name_ch = request.POST.get('name_ch')     # 中文名称
        game.desc = request.POST.get('desc')                        # 描述（英文）
        game.desc_ch = request.POST.get('desc_ch')                     # 描述（中文）
        game.star = request.POST.get('star')       # 星级

        game.icon_id = request.POST.get('icon')          # 图标文件_id
        game.rec_screen_id = request.POST.get('rec_screen')          # 推荐图片_id

        game.tag_ids = request.POST.get('tags', '')          # 标签_ids
        game.screen_ids = request.POST.get('screens', '')          # 截图文件_ids

        game.flash_id = request.POST.get('flash')          # flash文件_id
        game.apk_id = request.POST.get('apk')          # apk文件_id
        game.ipa_id = request.POST.get('ipa')          # apk文件_id
        game.apk_pack_id = request.POST.get('apk_pack')         # 本地应用商店打包文件

        ret =  game_service.update_game(game)
        return HttpResponse(ret.to_json())

    def list(self, request, template='game/game_list.html'):
        """
        展示所有游戏
        """
        tag_list = Tag.objects.all()
        category_list = Category.objects.all()
        game_list = Game.objects.all()

        return render(request, template, locals())

    def tail(self, request, id, template='game/game_tail.html'):
        """
        游戏详细信息
        """
        game = Game.objects.get(id=id)

        return render(request, template, locals())


game_views = Views()