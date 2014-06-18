# -*- coding:utf-8 -*-

from src.misc import Result
from src.misc.base.service import BaseService
from src.misc.debug import log_debug

from src.app.game.models import Tag


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
        return ret

    def delete_tag(self, id):
        """
       删除游戏系列
        """
        ret = Result()
        try:
            tag = Tag.objects.get(id=id)
            count = tag.game_tag_map.count()
            if count != 0:
                ret.success = False
                ret.msg = u"还有%s款游戏使用该标签，不能删除该标签" % count
                return  ret

            tag.delete()
        except Exception, e:
            log_debug.error(u"删除游戏标签<id:%s>，数据库操作失败，%s" % (id, e))
            ret.success = False
            ret.msg = u"数据库操作失败"
        return ret

tag_service = Service()