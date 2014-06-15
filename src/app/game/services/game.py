# -*- coding:utf-8 -*-

from src.misc import Result
from src.misc.base.service import BaseService
from src.misc.debug import log_debug


__all__ = ['game_service']


class Service(BaseService):

    def update_game(self, game):
        """
       编辑游戏
        """
        ret = Result()
        try:
            if not game.id:
                game.save()
            else:
                game.save_most()
            game.tags.clear()
            map(game.tags.add, [item.strip() for item in game.tag_ids.split(',') if item.strip()])
            game.screens.clear()
            map(game.screens.add, [item.strip() for item in game.screen_ids.split(',') if item.strip()])
        except Exception, e:
            log_debug.error(u"更新游戏<%s>，数据库操作失败，%s" % (game.name_ch, e))
            ret.success = False
            ret.msg = u"数据库操作失败"
            raise e
        return ret

game_service = Service()