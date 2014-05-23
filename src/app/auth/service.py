# -*- coding:utf-8 -*-

from src.misc import Result
from src.misc.base.service import BaseService


__all__ = ['auth_service']

USER_NAME = 'admin'
PASSWD = 'admin'


class Service(BaseService):

    def _get_user(self):
        return USER_NAME

    def _get_pwd(self):
        return PASSWD

    def auth_user(self, username, passwd):
        """
        用户名、口令认证用户
            @username: 用户名
            @passwd: 口令
        """
        ret = Result()
        if username != self._get_user():
            ret.success = False
            ret.msg = u'用户不存在'
            return ret
        if passwd != self._get_pwd():
            ret.success = False
            ret.msg = u'口令不正确'
        return ret


auth_service = Service()