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
    二、定义序列化器类
        1.必须得继承Serializer类或者Serializer子类
        2.定义的序列化器类中，字段名要与模型类中的字段名保持一致
        3.定义的序列化器类的字段（类属性）为Field子类
        4.默认定义哪些字段，那么哪些字段就会返回前端，同时也必须的输入（前端需要传递）
        5.常用的序列化器字段类型
            IntegerField  -> int
            CharField     -> str
            BooleanField  -> bool
            DateTimeField -> datetime
        6.可以在序列化器字段中指定不同的选项
            label和help_text，与模型类中的verbose_name和help_text参数一样
            IntegerField，可以使用max_value指定最大值，min_value指定最小值
            CharField，可以使用max_length指定最大长度，min_length指定最小长度
        7.定义的序列化器字段中，required默认为True，说明默认定义的字段必须得输入和输出
        8.如果在序列化器字段中，设置required=False，那么前端用户可以不传递该字段（校验时会忽略改该字段，所以不会报错）
        9.如果未定义模型类中的某个字段，那么该字段不会输入，也不会输出
        10.前端必须的输入（反序列化输入）name（必须得校验），但是不会需要输出（序列化器输出）？
            如果某个参数指定了write_only=True，那么该字段仅仅只输入（反序列化输入，做数据校验），不会输出（序列化器输出），
            默认write_only为False
        11.前端可以不用传递，但是后端需要输出？
            如果某个参数指定了read_only=True，那么该字段仅仅只输出（序列化器输出），不会输入（反序列化输入，做数据校验），
            默认read_only为False
        12.在序列化器类中定义的字段，默认allow_null=False，该字段不允许传递null空值，
            如果指定allow_null=True，那么该字段允许传递null
        13.在序列化器类中定义CharField字段，默认allow_blank=False，该字段不允许传递空字符串，
            如果指定allow_blank=True，那么该字段允许传递空字符串
        14.在序列化器类中定义的字段，可以使用default参数来指定默认值，如果指定了default参数，那么前端用户可以不用传递，
            会将default指定的值作为入参
    '''
    # id = serializers.IntegerField(label='项目id', help_text='项目id', max_value=1000, min_value=1)
    # name = serializers.CharField(label='项目名称', help_text='项目名称', max_length=20, min_length=5, write_only=True)
    # name = serializers.CharField(label='项目名称', help_text='项目名称', max_length=20, min_length=5, read_only=True)
    name = serializers.CharField(label='项目名称', help_text='项目名称', max_length=20, min_length=5)
    # leader = serializers.CharField(label='项目负责人', help_text='项目负责人', allow_null=True)
    # leader = serializers.CharField(label='项目负责人', help_text='项目负责人', allow_blank=True)
    leader = serializers.CharField(label='项目负责人', help_text='项目负责人', default='阿名')
