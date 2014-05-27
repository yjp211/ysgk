# -*- coding:utf-8 -*-

from django.db import models


class Image(models.Model):
    """
    图片文件
    """
    name = models.CharField(max_length=1024, blank=True)        # 文件名
    size = models.IntegerField(blank=True)                      # 文件大小
    width = models.IntegerField(blank=True)                     # 图片宽度（px）
    height = models.IntegerField(blank=True)                    # 图片高度(px)
    url = models.CharField(max_length=2048)                     # 云端地址

    class Meta:
        db_table = 'image'


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

    create_time = models.DateTimeField()            # 创建时间
    update_time = models.DateTimeField()            # 最后更新时间

    name = models.CharField(max_length=1024)        # 英文名称
    name_ch = models.CharField(max_length=1024)     # 中文名称

    desc = models.TextField()                       # 描述（英文）
    desc_ch = models.TextField()                    # 描述（中文）

    tags = models.ManyToManyField(Tag, through='GameTagMaps')

    #所有图片单独存储在一个表中， 指定"related_name" ORM会而外的创建关系表
    icon = models.ForeignKey(Image, related_name='icon_image')        # 图标
    screens = models.ManyToManyField(Image, related_name='screen_images')   # 截图，多个
    rec_screens = models.ManyToManyField(Image, related_name='recommand_screens')   # 推荐截图

    #flash, app, apk上传后，将其存储到云端，数据库中保留云端的下载路径
    flash_url = models.CharField(max_length=2048)  # 原始flash文件（保存到云端，数据库存储云端的下载地址）
    ipa_url = models.CharField(max_length=2048, blank=True)    # 上传的ios文件（保存到云端，数据库存储云端的下载地址）
    apk_url = models.CharField(max_length=2048)    # 制作成的apk文件（保存到云端，数据库存储云端的下载地址）

    class Meta:
        db_table = 'game'


class GameTagMaps(models.Model):
    """
    游戏和标签的映射关系
    """
    game = models.ForeignKey(Game)
    tags = models.ForeignKey(Tag)

    class Meta:
        db_table = 'game_tag_maps'