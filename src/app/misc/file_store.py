# -*- coding:utf-8 -*-

import time
import urllib2
import upyun

from src.misc import Result
from src.settings import UPYUN

from src.misc.debug import log_debug


__all__ = ['store']


class FielNameIsNone(Exception):
    pass


class FielUrlIsNone(Exception):
    pass


class BaseStore(object):

    def gen_file_path(self, db_file):
        pass

    def parse_file_path(self, db_file):
        pass

    def save_file(self, db_file):
        pass

    def delete_file(self, db_file):
        pass


class UpyunStore(BaseStore):

    def __init__(self):
        self.up = upyun.UpYun(UPYUN['BUCKETNAME'], UPYUN['USERNAME'],
                              UPYUN['PASSWORD'], timeout=UPYUN['TIMEOUT'], endpoint=upyun.ED_AUTO)
        self.url_prefix = "http://%s.b0.upaiyun.com" % (UPYUN['BUCKETNAME'])

    def gen_file_path(self, db_file):
        if db_file.name is None or len(db_file.name) == 0:
            raise FielNameIsNone()
        file_path = u"%s_%s" % (time.time(), db_file.name)
        db_file.url =  "%s/%s" % (self.url_prefix, file_path)
        return file_path

    def parse_file_path(self, db_file):
        if db_file.url is None or len(db_file.url) == 0:
            raise FielUrlIsNone()
        return db_file.url[len(self.url_prefix):]

    def save_file(self, db_file):
        ret = Result()
        try:
            self.up.put(self.gen_file_path(db_file), db_file.body.read())

        except Exception, e:
            log_debug.error(u"upyun上传文件<%s>失败，%s" % (db_file.name, e))
            ret.success = False
            ret.exception = e
            ret.msg = e.message
        return ret

    def delete_file(self, db_file):
        ret = Result()
        try:
            self.up.delete(self.parse_file_path(db_file))
        except Exception, e:
            log_debug.error(u"upyun删除文件<%s>失败，%s" % (db_file.name, e))
            ret.success = False
            ret.exception = e
            ret.msg = e.message
        return ret


store = UpyunStore()