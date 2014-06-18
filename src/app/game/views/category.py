# -*- coding:utf-8 -*-
from django.shortcuts import render, HttpResponse

from src.misc.base.view import require_post
from src.misc.base.view import BaseView

from src.app.game.models import Category
from src.app.game.services.category import category_service

__all__ = ['category_views']


class Views(BaseView):
    """
    游戏系列管理视图
    """

    def list(self, request, template='game/category_list.html'):
        """
        展示所有游戏系列
        """
        category_list = Category.objects.all()

        return render(request, template, locals())

    def prepar_update(self, request, id='', template='game/category_update.html'):
        """
        进入游戏系列编辑界面
        """
        category_list = Category.objects.all()
        if id:
            obj = category_list.get(id=id)

        return render(request, template, locals())

    @require_post
    def update(self, request):
        """
        添加或修改系列
        """
        category = Category()
        category.id = request.POST.get('id', None)       # 英文名称
        category.name = request.POST.get('name')       # 英文名称
        category.name_ch = request.POST.get('name_ch')     # 中文名称
        category.desc = request.POST.get('desc')                        # 描述（英文）
        category.desc_ch = request.POST.get('desc_ch')                     # 描述（中文）

        category.icon_id = request.POST.get('category_icon')    # 系列图标

        ret =  category_service.update_category(category)
        return HttpResponse(ret.to_json())

    def delete(self, request, id):
        """
        删除系列
        """
        ret =  category_service.delete_category(id)
        return HttpResponse(ret.to_json())

category_views = Views()