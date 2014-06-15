# -*- coding:utf-8 -*-

from src.misc import Result
from src.misc.base.service import BaseService
from src.misc.debug import log_debug


from src.app.game.models import GameCategory

__all__ = ['game_service']


class Service(BaseService):

    def _update_category(self, game):
        """
        游戏系列维护
        update_game只负责加入、移除系列。当重复加入系列时，不能将原有的系列删除，防止数据被重置
        :param game:
        :return:
        """
        gamecategory_set = game.gamecategory_set.all()
        old_ids = [ int(item.category.id) for item in gamecategory_set ]
        new_ids = [ int(item.strip()) for item in game.category_ids.split(',') if item.strip() ]
        print old_ids, new_ids
        #去掉老的
        for item in gamecategory_set:
            if item.category.id not in new_ids:
                item.delete()

        #增加新的
        for id in new_ids:
            if id not in old_ids:
                game_category = GameCategory()
                game_category.game_id = game.id
                game_category.category_id = id
                game_category.save()




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

            self._update_category(game)
        except Exception, e:
            log_debug.error(u"更新游戏<%s>，数据库操作失败，%s" % (game.name_ch, e))
            ret.success = False
            ret.msg = u"数据库操作失败"
            raise e
        return ret

game_service = Service()