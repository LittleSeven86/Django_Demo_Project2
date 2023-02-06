#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :serializers.py
# @Time      :2023/2/6 21:13
# @Author    :LittleSeven
# @Address   ：https://gitee.com/linguchong/Demo1_1.git

from rest_framework import serializers


'''
一、序列化器
    a.如果需要使用DRF框架来实现序列化、反列化、数据操作，在子应用中创建serializers.py文件
    b.文件名推荐命名为serializers.py
    
'''

class ProjectSerializer(serializers.Serializer):
    '''

    '''
    id = serializers.IntegerField()
    name = serializers.CharField()
    leader = serializers.CharField()
