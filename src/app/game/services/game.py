# -*- coding:utf-8 -*-
from django.db.models import Q

from src.misc import Result
from src.misc.base.service import BaseService
from src.misc.debug import log_debug


from src.app.game.models import Game, GameCategory

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

    def delete_game(self, id):
        """
       编辑游戏
        """
        ret = Result()
        try:
            game = Game.objects.get(id=id)
            if game.icon:
                game.icon.delete()
            if game.rec_screen:
                game.rec_screen.delete()
            if game.flash:
                game.flash.delete()
            if game.ipa:
                game.ipa.delete()
            if game.apk:
                game.apk.delete()
            if game.apk_pack:
                game.apk_pack.delete()
            game.screens.all().delete()

            game.delete()
        except Exception, e:
            log_debug.error(u"删除游戏<id:%s>，数据库操作失败，%s" % (id, e))
            ret.success = False
            ret.msg = u"数据库操作失败"
            raise e
        return ret

    def query_game(self, query_option):
        """
        根据查询条件显示游戏
        :param query_form:
        :return:
        """
        ret = Result()
        game_list = Game.objects.all()
        if query_option:
            key_word = query_option.get('key_word')
            if key_word:
                game_list = game_list.filter(Q(name__contains=key_word)
                                              | Q(name_ch__contains=key_word)
                                              | Q(desc__contains=key_word)
                                              | Q(desc_ch__contains=key_word))
            tag_ids = query_option.get('tags')
            if tag_ids:
                for id in tag_ids.split(','):
                    if id.strip():
                        game_list = game_list.filter(tags=id.strip())

            category_ids = query_option.get('categorys')
            if category_ids:
                for id in category_ids.split(','):
                    if id.strip():
                        game_list = game_list.filter(categorys=id.strip())

            sort_field = query_option.get('sort_field')
            if sort_field:
                sort_type = query_option.get('sort_type', 'asce')
                if sort_type == 'desc':
                    sort_field = '-%s' % sort_field
                game_list = game_list.order_by(sort_field)
                #gamecategory__rank
        ret.data['game_list'] = game_list
        return ret


game_service = Service()