# -*- coding:utf-8 -*-

from django.db import models

from src.misc.base.model import BaseModel, FIELD_NAME_MAX_LENGTH, FIELD_URL_MAX_LENGTH


class File(BaseModel):
    """
    文件
    """
    create_time = models.DateTimeField(auto_now_add=True)            # 创建时间

    name = models.CharField(max_length=FIELD_NAME_MAX_LENGTH)        # 文件名
    use_on = models.CharField(max_length=FIELD_NAME_MAX_LENGTH, blank=True)
    mini_type = models.CharField(max_length=FIELD_NAME_MAX_LENGTH, blank=True)
    width = models.IntegerField(blank=True, null=True)                     # 图片宽度（px）
    height = models.IntegerField(blank=True, null=True)                    # 图片高度(px)
    size = models.IntegerField()                                       # 文件大小
    url = models.CharField(max_length=FIELD_URL_MAX_LENGTH)                      # 云端地址

    class Meta:
        db_table = 'game_file'


class Tag(BaseModel):
    """
    游戏的标签类型
    """
    create_time = models.DateTimeField(auto_now_add=True)            # 创建时间
    update_time = models.DateTimeField(auto_now=True)            # 最后更新时间
    name = models.CharField(max_length=FIELD_NAME_MAX_LENGTH)        # 标签名称
    name_ch = models.CharField(max_length=FIELD_NAME_MAX_LENGTH)     # 标签的中文名称
    desc = models.TextField(null=True, blank=True)                       # 描述（英文）
    desc_ch = models.TextField(null=True, blank=True)                    # 描述（中文）

    class Meta:
        db_table = 'game_tag'


class Category(BaseModel):
    """
    游戏系列
    """

    create_time = models.DateTimeField(auto_now_add=True)            # 创建时间
    update_time = models.DateTimeField(auto_now=True)            # 最后更新时间
    name = models.CharField(max_length=FIELD_NAME_MAX_LENGTH)        # 英文名称
    name_ch = models.CharField(max_length=FIELD_NAME_MAX_LENGTH)     # 中文名称
    desc = models.TextField(null=True, blank=True)                       # 描述（英文）
    desc_ch = models.TextField(null=True, blank=True)                    # 描述（中文）
    icon = models.ForeignKey(File, related_name='category_icon_map', null=True, blank=True, on_delete=models.SET_NULL)        # 系列图标

    class Meta:
        db_table = 'game_category'


class Game(BaseModel):
    """
    游戏模型
    """

    create_time = models.DateTimeField(auto_now_add=True)            # 创建时间
    update_time = models.DateTimeField(auto_now=True)            # 最后更新时间

    name = models.CharField(max_length=FIELD_NAME_MAX_LENGTH)        # 英文名称
    name_ch = models.CharField(max_length=FIELD_NAME_MAX_LENGTH)     # 中文名称

    desc = models.TextField()                       # 描述（英文）
    desc_ch = models.TextField()                    # 描述（中文）

    star = models.IntegerField(default=4)   # 游戏星级 [1..5]

    tags = models.ManyToManyField(Tag, related_name='game_tag_map')

    #所有图片单独存储在一个表中， 指定"related_name" ORM会而外的创建关系表
    icon = models.ForeignKey(File, related_name='game_icon_map', null=True, blank=True, on_delete=models.SET_NULL)        # 图标被删除后不会删除游戏
    screens = models.ManyToManyField(File, related_name='game_screens_map', null=True, blank=True)   # 截图，多个
    rec_screen = models.ForeignKey(File, related_name='game_rec_screen_map', null=True, blank=True, on_delete=models.SET_NULL)   # 推荐截图

    #flash, app, apk上传后，将其存储到云端，数据库中保留云端的下载路径
    # 原始flash文件（保存到云端，数据库存储云端的下载地址）
    flash = models.ForeignKey(File, related_name='game_flash_map', null=True, blank=True, on_delete=models.SET_NULL)

    # 上传的ios文件（保存到云端，数据库存储云端的下载地址）
    ipa = models.ForeignKey(File, related_name='game_ipa_map', null=True, blank=True, on_delete=models.SET_NULL)
    # 制作成的apk文件（保存到云端，数据库存储云端的下载地址）
    apk = models.ForeignKey(File, related_name='game_apk_map', null=True, blank=True, on_delete=models.SET_NULL)
    # 本地应用商店的android包下载地址
    apk_pack = models.ForeignKey(File, related_name='local_android_package', null=True, blank=True, on_delete=models.SET_NULL)

    categorys = models.ManyToManyField(Category, through='GameCategory')

    class Meta:
        db_table = 'game_game'


class GameCategory(BaseModel):
    """
    游戏系列映射
    """
    create_time = models.DateTimeField(auto_now_add=True)            # 创建时间
    stick_time = models.DateTimeField(null=True, blank=True)       # 置顶时间
    game = models.ForeignKey(Game)     # 对应的游戏
    category = models.ForeignKey(Category) # 对应的系列
    rank = models.IntegerField(default=1)   # 游戏排行 权值 [1..100]

    class Meta:
        db_table = 'game_categorys'
        unique_together = ('game', 'category')   #联合主键