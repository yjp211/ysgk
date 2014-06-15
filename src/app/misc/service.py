# -*- coding:utf-8 -*-

from src.misc import Result
from src.misc.base.service import BaseService
from src.misc.debug import log_debug

from src.app.misc.file_store import store
from src.app.game.models import File


__all__ = ['misc_service']


class Service(BaseService):
    """
    处理一些公共业务
    """

    def upload_file(self, upload_file):
        """
        上传文件
        """
        ret = Result()
        upload_ret = store.save_file(upload_file)
        if not upload_ret.success:
            ret.success = False
            ret.msg = u"上传云端失败"
        else:
            try:
                #保存到数据库
                upload_file.save()
            except Exception, e:
                log_debug.error(u"上传文件，数据库保存失败，%s" % e)
                ret.success = False
                ret.msg = u"数据库操作失败"
                #删除文件
                store.delete_file(upload_file)
        ret.data['file_id'] = upload_file.id
        return ret

    def delete_file(self, file_id):
        """
        删除文件
        """
        ret = Result()
        #获取到对象
        try:
            delete_file = File.objects.get(id=file_id)
        except Exception, e:
            log_debug.error(u"删除文件，数据库获取对象失败，%s" % e)
            ret.success = False
            ret.msg = u"数据库操作失败，对象可能不存在"
            return ret
        #删除云端
        delete_ret = store.delete_file(delete_file)
        if delete_ret.success:
            try:
                delete_file.delete()
            except Exception, e:
                log_debug.error(u"删除文件，数据库操作失败，%s" % e)
                ret.success = False
                ret.msg = u"数据库操作失败"
        else:
            ret.success = False
            ret.msg = u"云端删除失败"
            #删除文件

        return ret


misc_service = Service()