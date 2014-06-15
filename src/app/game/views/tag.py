# -*- coding:utf-8 -*-
from django.shortcuts import render, HttpResponse

from src.misc.base.view import require_post
from src.misc.base.view import BaseView

from src.app.game.models import Tag
from src.app.game.services.tag import tag_service

__all__ = ['tag_views']


class Views(BaseView):
    """
    游戏标签管理视图
    """

    def list(self, request, template='game/tag_list.html'):
        """
        展示所有游戏标签
        """
        tag_list = Tag.objects.all()

        return render(request, template, locals())

    def prepar_update(self, request, id='', template='game/tag_update.html'):
        """
        进入游戏标签编辑界面
        """
        tag_list = Tag.objects.all()
        if id:
            obj = tag_list.get(id=id)
        return render(request, template, locals())

    @require_post
    def update(self, request):
        """
        添加或修改标签
        """
        tag = Tag()
        tag.id = request.POST.get('id', None)       # 英文名称
        tag.name = request.POST.get('name')       # 英文名称
        tag.name_ch = request.POST.get('name_ch')     # 中文名称
        tag.desc = request.POST.get('desc')                        # 描述（英文）
        tag.desc_ch = request.POST.get('desc_ch')                     # 描述（中文）

        ret =  tag_service.update_tag(tag)
        return HttpResponse(ret.to_json())



tag_views = Views()