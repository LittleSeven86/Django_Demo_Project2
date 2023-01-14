#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :base_model.py
# @Time      :2023/1/9 20:37
# @Author    :LittleSeven
# @Address   ：https://github.com/MengZhang893/Demo1_1.git

from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='id主键', help_text='id主键')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间', help_text='更新时间')

    class Meta:
        # 在内部类Meta中，一旦指定abstract = True，那么当前模型类为抽象模型类，在迁移时不会创建表，仅仅是为了其他类继承
        abstract = True
