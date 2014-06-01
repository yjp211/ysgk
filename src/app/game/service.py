# -*- coding:utf-8 -*-

from src.misc import Result
from src.misc.base.service import BaseService



__all__ = ['game_service']


class Service(BaseService):



    def add_game(self):
        """
       添加游戏
        """
        ret = Result()
        return ret


game_service = Service()