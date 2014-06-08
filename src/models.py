# -*- coding:utf-8 -*-

from django.db import models


FILED_NORMAL_MAX_LENGTH = 1024
FIELD_NAME_MAX_LENGTH = 1024
FIELD_URL_MAX_LENGTH = 2048


class File(models.Model):
    """
    文件
    """
    create_time = models.DateTimeField(auto_now_add=True)            # 创建时间

    name = models.CharField(max_length=FIELD_NAME_MAX_LENGTH)        # 文件名
    mini_type = models.CharField(max_length=FILED_NORMAL_MAX_LENGTH, blank=True)
    size = models.IntegerField()                                       # 文件大小
    url = models.CharField(max_length=FIELD_URL_MAX_LENGTH)                      # 云端地址

    class Meta:
        db_table = 'file'


class Image(File):
    """
    图片文件
    """
    width = models.IntegerField(blank=True)                     # 图片宽度（px）
    height = models.IntegerField(blank=True)                    # 图片高度(px)

    class Meta:
        db_table = 'image'

    class FileMeta:
        exclude_fields = []
        exclude_fields_append = ['id', 'lft', 'rght', 'tree_id', 'parent']



class Tag(models.Model):
    """
    游戏的标签类型
    """
    name = models.CharField(max_length=1024)        # 标签名称
    name_ch = models.CharField(max_length=1024)     # 标签的中文名称

    class Meta:
        db_table = 'tag'


class Game(models.Model):
    """
    游戏模型
    """

    create_time = models.DateTimeField(auto_now_add=True)            # 创建时间
    update_time = models.DateTimeField(auto_now=True)            # 最后更新时间

    name = models.CharField(max_length=1024)        # 英文名称
    name_ch = models.CharField(max_length=1024)     # 中文名称

    desc = models.TextField()                       # 描述（英文）
    desc_ch = models.TextField()                    # 描述（中文）

    tags = models.ManyToManyField(Tag, related_name='game_tag_map')

    #所有图片单独存储在一个表中， 指定"related_name" ORM会而外的创建关系表
    icon = models.ForeignKey(File, related_name='game_icon_map')        # 图标
    screens = models.ManyToManyField(File, related_name='game_screens_map')   # 截图，多个
    rec_screen = models.ForeignKey(File, related_name='game_rec_screen_map')   # 推荐截图

    #flash, app, apk上传后，将其存储到云端，数据库中保留云端的下载路径
    flash = models.ForeignKey(File, related_name='game_flash_map')  # 原始flash文件（保存到云端，数据库存储云端的下载地址）
    ipa = models.ForeignKey(File, related_name='game_ipa_map', blank=True)    # 上传的ios文件（保存到云端，数据库存储云端的下载地址）
    apk = models.ForeignKey(File, related_name='game_apk_map')    # 制作成的apk文件（保存到云端，数据库存储云端的下载地址）

    class Meta:
        db_table = 'game'

