# -*- coding:utf-8 -*-

from src.misc import Result
from src.misc.base.service import BaseService
from src.misc.debug import log_debug



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
            raise e
        return ret

category_service = Service()