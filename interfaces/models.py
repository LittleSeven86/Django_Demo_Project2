from django.db import models

# from utils.base_model import BaseModel

from utils import base_model

# from projects.models import Projects


'''
1、表与表之间有哪些关系？
    -Projects与Interfaces表，一对多关系
    -学生表与学生详细信息表，一对一关系
    -学生表与课程表，多对多的关系
'''


# class Interfaces(models.Model):
class Interfaces():
    # id = models.AutoField(primary_key=True, verbose_name='id主键', help_text='id主键')
    name = models.CharField(verbose_name='接口名称', help_text='接口名称', max_length=20, unique=True)
    tester = models.CharField(verbose_name='测试人员', help_text='测试人员', max_length=10)
    '''
    a.如果需要创建一对多的外键，那么会在“多”的那一个模型类中定义外键字段
    b.如果创建的是一对多的关系，使用ForeignKey
    c.如果创建的是一对一的关系，可以在任何一个模型类使用OneToOneField
    d.如果创建的是多对多的关系，可以在任何一个模型类使用ManyToManyField
    e.ForeignKey第一个参数为必传参数，指定需要关联的父表模型类
        方式一：直接使用父表模型类的引用
        方式二：可以使用'子应用名称.父表模型类名'（推荐）
    f.ForeignKey需要使用on_delete指定级联删除策略
        CASCADE： 当父表数据删除时，相对应的从表数据会被自动删除
        SET_NULL：当父表数据删除时，相对应的从表数据会被自动设置为null值
        PROTECT：当父表数据删除时，如果有相对应的从表数据会抛出异常
        ET_DEFAULT: 当父表数据删除时，相对应的从表数据会被自动设置为默认值，还需要额外指定default=True
    '''
    # projects = models.ForeignKey(Projects)
    # models.ManyToManyField
    projects = models.ForeignKey('projects.Projects', on_delete=models.CASCADE,verbose_name='所属项目', help_text='所属项目')

    # create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    # update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间', help_text='更新时间')

    class Meta:
        # db_table指定创建的数据表名称
        db_table = 'tb_interfaces'
        # 为当前数据表设置中文描述信息
        verbose_name = '接口表'
        verbose_name_plural = '接口表'
        ordering = ['id']

    def __str__(self):
        return f"Interfaces({self.name})"
