# -*- coding: utf-8 -*-

import  json

class Result(object):
    """
    function return result instance
    """

    def __init__(self):
        self.success = True  # True/False
        self.msg = ''        # message
        self.errno = ''      # error number
        self.exception = ''   # if have a exception, save it
        self.data = {}        # a dict contain value

    def to_json(self):
        return json.dumps(vars(self))

    def __unicode__(self):
        if self.success:
            return u'成功：<%s>' % self.msg
        else:
            return u'失败：%s<%s>%s' % (self.errno and '<%s>' % self.errno or '',
                                     self.msg,
                                     self.exception and '<%s>' % self.exception or '')
