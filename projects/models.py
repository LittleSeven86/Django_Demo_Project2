from django.db import models
from utils.base_model import BaseModel


# Create your models here.
class Animal(models.Model):
    '''
    1、一般在子应用models.py中定义模型类(相当于数据库中的一张表)
    2、必须继承Model或者Model子类
    3、在模型类中定义类属性(必须得为Field子类)相当于数据表中的字段
        4、Charfiled --> varchar
        5、IntegerField --> integer
        6、BooleanField --> bool
    7、在migration里，存放迁移脚本：
        python manage.py makemigrations 子应用名称(加子应用名称，可以指定迁移，不然全部进行迁移生成迁移脚本)
    8、查看迁移脚本生成的SQL语句 python manage.py sqlmigrate 子应用名 迁移脚本名(无需加py)
    9、生成的数据表名称默认为：子应用名_模型类名
    10、默认会自动创建一个名为id的自增主键
    '''
    # varchar 不固定长度字符串，可以设定最大长度
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.BooleanField()


class Projects(BaseModel):
    '''
    1、CharField类型必须指定max_length(该字段的最大字节数)
    2、如果需要给一个字段添加唯一约束，可以将unique设置为True，(默认为False)
    '''
    ids = models.IntegerField(primary_key=True, verbose_name='项目主键', help_text='项目主键')
    name = models.CharField(max_length=20, verbose_name='项目名称', help_text='项目名称', unique=True)
    leader = models.CharField(max_length=10, verbose_name='项目负责人', help_text='项目负责人')
    # 3、使用default指定默认值(如果指定默认值后，创建记录时，该字段不传递会使用默认值)
    is_excute = models.BooleanField(verbose_name='是否启动项目', help_text='是否启动项目', default=True)
    # 4、null=True指定，前端创建数据时，可以指定该字段为null，默认为null=False，DRF进行反序列化器输入时才有效
    # 5、blank=True指定，前端创建数据时，可以指定该字段为空字符串''，默认为null=False，DRF进行反序列化器输入时才有效
    desc = models.TextField(verbose_name='项目描述信息', help_text='项目描述信息', null=True, blank=True, default='')
    # 6、在DateTimeField、DateField等字段中，指定auto_now_add=True，在创建一条记录时，会自动将创建记录时等时间作为该字段的值，后续在更新数据时，就不再修改
    # 7、在DateTimeField、DateField等字段中，指定auto_now=True，会自动将更新记录时等时间作为该字段的值
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间', help_text='更新时间')

    # 8、可以在任意一个模型类中创建Meta内部类，用于修改数据库的原数据信息
    class Meta:
        # db_table指定创建的数据表名称
        db_table = 'tb_projects'
        # 指定创建为当前数据表设置中文描述信息
        verbose_name = '项目表'
        verbose_name_plural = '项目表'
        # 添加默认排序功能，通过id进行排序
        ordering = ['id']
