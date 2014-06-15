# -*- coding:utf-8 -*-

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
        print self._meta.fields
        field_names = []
        for field in self._meta.fields:
            if not field.primary_key:
                if hasattr(self, field.name):
                    val = getattr(self, field.name)
                    if val is not None and  val is not field.default:
                        field_names.append(field.name)
        print field_names
        return self.save(update_fields=field_names)

    class Meta:
        abstract = True