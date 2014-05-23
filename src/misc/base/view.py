# -*- coding:utf-8 -*-

import inspect

from django.http.response import HttpResponseNotAllowed, HttpResponseServerError

from src.misc.debug import log_view



__all__ = ['BaseView', 'require_get', 'require_post']


def view_wrap(func):
    """
    对view func进行包装
        debug日志记录
    """
    def wrapped(request, *args, **kwargs):
        # __doc__ encode as ascii
        # and we only need the first line
        doc = func.__doc__
        description = doc.strip().split('\n')[0].decode('utf-8')

        log_view.debug(u'<%s:%s> %s [ 参数 GET：%s，POST：%s ]' %
                       (func.__module__, func.__name__, description, request.GET.items(), request.POST.items()))
        try:
            response = func(request, *args, **kwargs)
            log_view.debug(u'%s [ http状态码，%s ]' % (description, response.status_code))
            return response
        except Exception, e:
            log_view.error(u'%s [ 出现异常，%s ]' % (description, e))
            raise

    return wrapped


class BaseView(object):
    """
    所有的View都从该类继承
    """

    def __getattribute__(self, name):
        value = object.__getattribute__(self, name)
        if inspect.ismethod(value):
            if str(name).startswith('_'):
                return value
            return view_wrap(value)
        else:
            return value


def require_method(method):
    """
    request的请求类型必须为 [method]
    @param method: POST|GET
    """
    def func(function=None):
        def _filter(self, request, *args, **kwargs):

            if request.method != method:
                log_view.error(u"request<%s:%s>请求类型必须为<%s>，当前为<%s>" % \
                    (function.__module__, function.__name__, method, request.method))
                return HttpResponseNotAllowed([method])
            else:
                return function(self, request, *args, **kwargs)

        # 将__doc__ 传递下去，否则会引起异常
        _filter.__doc__ = function.__doc__
        _filter.__module__ = function.__module__
        _filter.__name__ = function.__name__

        return _filter
    return func

require_get = require_method('GET')

require_post = require_method('POST')