# -*- coding:utf-8 -*-
import json
from django.shortcuts import HttpResponse
from src.settings import OPEN_API_URL_PREFIX

def config(request):
    """
    接口配置
    """
    config = {
        "version": "1.0",
        "versionCheckURL": "",
        "hotGamesURL": "%s/game/category/hot/" % OPEN_API_URL_PREFIX.rstrip('/'),
        "categoriesURL": "%s/game/categories/" % OPEN_API_URL_PREFIX.rstrip('/'),
    }
    return HttpResponse(json.dumps(config))
