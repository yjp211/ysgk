# -*- coding:utf-8 -*-

from src.misc import Result
from src.misc.base.service import BaseService
from src.misc.debug import log_debug

from src.app.game.models import Category



__all__ = ['category_service']


class Service(BaseService):

    def update_category(self, category):
        """
       编辑游戏系列
        """
        ret = Result()
        try:
            if not category.id:
                category.save()
            else:
                category.save_most()
        except Exception, e:
            log_debug.error(u"更新游戏系列<%s>，数据库操作失败，%s" % (tag.name_ch, e))
            ret.success = False
            ret.msg = u"数据库操作失败"
        return ret

    def delete_category(self, id):
        """
       删除游戏系列
        """
        ret = Result()
        try:
            category = Category.objects.get(id=id)
            count = category.game_set.count()
            if count != 0:
                ret.success = False
                ret.msg = u"系列中还有%s款游戏，不能删除该系列" % count
                return  ret
            if category.icon:
                category.icon.delete()

            category.delete()
        except Exception, e:
            log_debug.error(u"删除游戏系列<id:%s>，数据库操作失败，%s" % (id, e))
            ret.success = False
            ret.msg = u"数据库操作失败"
        return ret

category_service = Service()