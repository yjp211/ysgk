# -*- coding:utf-8 -*-
from django.shortcuts import HttpResponse

from src.misc.base.view import BaseView

from src.api.game.services import service

__all__ = ['views']




class Views(BaseView):
    """
    游戏API接口
    """

    def get_all_category(self, request):
        """
        获取所有游戏系列
        """
        ret = service.get_all_category()
        if ret.success:
            json_data = ret.data.get('json_data', '[]')
        else:
            json_data = '[]'
        return HttpResponse(json_data)

    def list_hot_category(self, request):
        """
        获取热门游戏系列
        """
        page_num = request.GET.get('pageNum', '0')
        page_size = request.GET.get('pageSize', '0')
        ret = service.list_hot_category(page_num, page_size)
        if ret.success:
            json_data = ret.data.get('json_data', '{}')
        else:
            json_data = '{}'
        return HttpResponse(json_data)

    def list_category(self, request, id):
        """
        获取指定游戏系列
        """
        page_num = request.GET.get('pageNum', '0')
        page_size = request.GET.get('pageSize', '0')
        ret = service.list_category(id, page_num, page_size)
        if ret.success:
            json_data = ret.data.get('json_data', '{}')
        else:
            json_data = '{}'
        return HttpResponse(json_data)

    def tail(self, request, id):
        """
        获取游戏详细信息
        """
        return HttpResponse()


views = Views()