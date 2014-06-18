# -*- coding:utf-8 -*-

import datetime
from django.db import models


__all__ = [
    'BaseModel',
    'FILED_NORMAL_MAX_LENGTH',
    'FIELD_NAME_MAX_LENGTH',
    'FIELD_URL_MAX_LENGTH'
    ]

FILED_NORMAL_MAX_LENGTH = 1024
FIELD_NAME_MAX_LENGTH = 1024
FIELD_URL_MAX_LENGTH = 2048
FILE_USE_ON = ['icon', 'screens', 'rec_screen', 'flash', 'apk', 'ipa', 'apk_pack']



class CustomManager(models.Manager):

    def all_id(self):
        return [ obj.id for obj in self.all() ]



class BaseModel(models.Model):
    objects = CustomManager()

    def save_most(self):
        field_names = []
        for field in self._meta.fields:
            if not field.primary_key:
                if hasattr(self, field.name):
                    val = getattr(self, field.name)
                    if val is not None and  val is not field.default:
                        field_names.append(field.name)
        print self._meta.get_all_field_names()
        if 'update_time' in self._meta.get_all_field_names():

            field_names.append('update_time')
            self.update_time = datetime.datetime.today()
        return self.save(update_fields=field_names)

    class Meta:
        abstract = True