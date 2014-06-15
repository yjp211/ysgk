# -*- coding:utf-8 -*-

from src.misc import Result
from src.misc.base.service import BaseService
from src.misc.debug import log_debug



__all__ = ['tag_service']


class Service(BaseService):

    def update_tag(self, tag):
        """
       编辑游戏标签
        """
        ret = Result()
        try:
            if not tag.id:
                tag.save()
            else:
                tag.save_most()
        except Exception, e:
            log_debug.error(u"更新游戏标签<%s>，数据库操作失败，%s" % (tag.name_ch, e))
            ret.success = False
            ret.msg = u"数据库操作失败"
            raise e
        return ret

tag_service = Service()