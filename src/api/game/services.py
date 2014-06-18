# -*- coding:utf-8 -*-
import json

from src.settings import OPEN_API_URL_PREFIX

from src.misc import Result
from src.misc.base.service import BaseService
from src.misc.debug import log_debug


from src.app.game.models import Category

__all__ = ['service']


class Service(BaseService):


    def get_all_category(self):
        """
        获取所有游戏系列
        """
        ret = Result()
        try:
            json_obj = []
            for item in Category.objects.all():
                item_dict = {
                    'name': item.name,
                    'name_ch': item.name_ch,
                    'desc': item.desc,
                    'desc_ch': item.desc_ch,
                    'icon': item.icon and item.icon.url or '',
                    'length': item.game_set.count(),
                    'gamesURL': '%s/game/category/%s/' % (OPEN_API_URL_PREFIX.rstrip('/'), item.id)
                }
                json_obj.append(item_dict)
            ret.data['json_data'] = json.dumps(json_obj)
        except Exception, e:
            log_debug.error(u"获取所有游戏系列失败，数据库操作失败，%s" % (e))
            ret.success = False
            ret.msg = u"数据库操作失败"
            raise e
        return ret

    def list_category(self, id, page_num, page_size):
        """
        获取系列的详细信息
        :param id: 系列id
        :param page_num: 当前第几页
        :param page_size: 每页大小
        :return:
        """
        ret = Result()
        try:
            if not page_num or int(page_num) < 1:
                page_num = 1
            if not page_size or int(page_size) < 1:
                page_size = 10
            page_num = int(page_num)
            page_size = int(page_size)
            game_arr = []
            json_obj = {
                'pageNum': page_num,
                'pageSize': page_size,
                'games': game_arr,
            }

            for item in Category.objects.get(id=id).game_set.all()\
                                .order_by('-gamecategory__stick_time', '-update_time') \
                                [(page_num-1)*page_size : page_num*page_size]:

                item_dict = {
                    'id': item.id,
                    'name': item.name,
                    'name_ch': item.name_ch,
                    'desc': item.desc,
                    'desc_ch': item.desc_ch,
                    'starValue': item.star,
                    'icon': item.icon and item.icon.url or '',
                    'snapshots': [ i.url for i in item.screens.all() ],
                    'packageName': item.apk_pack and item.apk_pack.name or '',
                    'size': item.apk_pack and item.apk_pack.size or 0,
                    'downloadURL': item.apk_pack and item.apk_pack.url or '',
                }
                game_arr.append(item_dict)
            ret.data['json_data'] = json.dumps(json_obj)
        except Exception, e:
            log_debug.error(u"获取游戏系列<id:%s>，数据库操作失败，%s" % (id, e))
            ret.success = False
            ret.msg = u"数据库操作失败"
            raise e
        return ret

    def list_hot_category(self, pageNum, pageSize):
        """
        获取热门游戏列表
        :param pageNum:
        :param pageSize:
        :return:
        """
        ret = Result()
        try:
            category = Category.objects.filter(name__iexact='hot')[0]

            return self.list_category(category.id, pageNum, pageSize)
        except Exception, e:
            log_debug.error(u"获取所有游戏系列失败，数据库操作失败，%s" % (e))
            ret.success = False
            ret.msg = u"数据库操作失败"
            raise e
        return ret

service = Service()