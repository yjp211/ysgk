# -*- coding:utf-8 -*-

from django.shortcuts import HttpResponse

from src.misc.base.view import require_post
from src.misc.base.view import BaseView
from src.app.misc.service import misc_service

from src.app.game.models import File


__all__ = ['misc_views']


class Views(BaseView):
    """
    公共处理的一些视图函数
    """

    @require_post
    def upload_file(self, request):
        """
        上传文件
        """
        post_file = request.FILES.get('file')
        upload_file = File()
        upload_file.name = post_file.name
        upload_file.use_on = request.POST.get('use_on')
        upload_file.size = post_file.size
        upload_file.body = post_file
        ret = misc_service.upload_file(upload_file)
        return HttpResponse(ret.to_json())

    @require_post
    def delete_file(self, request):
        """
        删除文件
        """
        file_id = request.POST.get('file_id')
        ret = misc_service.delete_file(file_id)
        return HttpResponse(ret.to_json())


misc_views = Views()