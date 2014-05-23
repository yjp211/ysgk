# -*- coding:utf-8 -*-

from src.misc import Result
from src.misc.base.service import BaseService



__all__ = ['game_service']


class Service(BaseService):



    def all_user(self):
        """
        获取所有用户
        """
        ret = Result()
        return ret


game_service = Service()