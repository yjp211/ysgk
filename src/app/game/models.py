# -*- coding:utf-8 -*-

from django.db import models

class Game(models.Model):

    id = models.IntegerField(primary_key=True)      # id
    create_time = models.DateTimeField()            # 创建时间
    update_time = models.DateTimeField()            # 最后更新时间

    name = models.CharField(max_length=1024)        # 英文名称
    name_ch = models.CharField(max_length=1024)     # 中文名称

    desc = models.TextField()                       # 描述（英文）
    desc_ch = models.TextField()                    # 描述（中文）

    tags = models.TextField()                       # 标签（英文）
    tags_ch = models.TextField()                    # 标签（中文）

    #所有图片单独存储，以ID为索引建立目录结构存储, 目录不要太深防止路径长度超过max_length
    icon_img = models.CharField(max_length=2048)         # 图标
    screens_imgs = models.CharField(max_length=2048)   # 截图，指向一个目录
    rec_screens_img = models.CharField(max_length=2048)  # 推荐截图

    #flash, app, apk单独存储
    flash_path = models.CharField(max_length=2048)  # 原始flash文件
    app_path = models.CharField(max_length=2048)    # 制作成的app文件
    apk_path = models.CharField(max_length=2048)    # 制作成的apk文件


    #下载地址列表
    ipa_url = models.URLField()



