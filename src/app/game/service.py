# -*- coding:utf-8 -*-

from src.misc import Result
from src.misc.base.service import BaseService
from src.misc.debug import log_debug


__all__ = ['game_service']


class Service(BaseService):

    def add_game(self, game):
        """
       添加游戏
        """
        ret = Result()
        try:
            game.save()
            map(game.tags.add, [item.strip() for item in game.tag_ids.split(',') if item.strip()])
            map(game.screens.add, [item.strip() for item in game.screen_ids.split(',') if item.strip()])
        except Exception, e:
            log_debug(u"添加游戏<%s>，数据库操作失败，%s" % (game.name_ch, e))
            ret.success = False
            ret.msg = u"数据库操作失败"
        return ret

game_service = Service()