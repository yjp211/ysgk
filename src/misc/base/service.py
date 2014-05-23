# -*- coding:utf-8 -*-

import inspect

from src.misc import Result
from src.misc.debug import log_service


def service_wrap(func):
    """
    对service func进行包装，包括异常处理和debug日志记录
    """
    def wrapped(*args, **kwargs):
        # __doc__ encode as ascii
        # and we only need the first line
        doc = func.__doc__
        description = doc.strip().split('\n')[0].decode('utf-8')

        log_service.debug(u'<%s:%s> %s [ 参数：<%s %s> ]' %
                          (func.__module__, func.__name__, description, args, kwargs))
        try:
            ret = func(*args, **kwargs)
            if ret.success:
                log_service.info(u'%s [ 成功 ]' % (description))
            else:
                log_service.error(u'%s [ 失败，%s ]' % (description, ret.msg))
            return ret
        except Exception, e:
            log_service.error(u'%s [ 出现异常，%s ]' % (description, e))
            ret = Result()
            ret.success = False
            ret.exception = e
            ret.msg = e.message
            return ret

    return wrapped


class BaseService(object):
    """
    所有的Service都从该类继承
    """

    def __getattribute__(self, name):
        value = object.__getattribute__(self, name)
        if inspect.ismethod(value):
            if str(name).startswith('_'):
                return value
            return service_wrap(value)
        else:
            return value