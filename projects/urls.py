#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :urls.py
# @Time      :2023/1/2 11:07
# @Author    :LittleSeven
# @Address   ：https://github.com/MengZhang893/Demo1_1.git

from django.urls import path,include
from projects import views
from . import views
from rest_framework import routers

'''
1、可以使用路由器对象，为视图集类自动生成路由条目,只有视图集才可以有
2、路由器对象默认只为通用action（create、list、retrieve、update、destroy）生成路由条目，自定义的action不会生成路由条目
3、创建SimpleRouter路由对象
'''
router = routers.SimpleRouter()
# DefaultRouter与SimpleRouter功能类似，仅有的区别为：DefaultRouter会自动生成一个根路由（显示获取数据的入口）
# router = routers.DefaultRouter()
'''
4、使用路由器对象调用register方法进行注册
5、prefix指定路由前缀
6、viewset指定视图集类，不可调用as_view，只需要传递视图集类即可
'''
router.register(r'projects',views.ProjectViewSet)

urlpatterns = [
    # path('get/', views.get_project),
    # path('create/',views.create_project),
    # path('put/', views.put_project),
    # path('delete/',views.delete_project)
    # 定义类试图的路由条目
    # 类型图.as_view() 进行调用
    # path('projects/',views.ProjectsView.as_view()),
    # path('projects/',views.ProjectViewSet.as_view({
    #     'get':'list',
    #     # 'get':'names',
    #     'post':'create'
    # })),
    # path('projects/<int:pk>/',views.ProjectsDetailView.as_view()),
    # path('projects/<int:pk>/',views.ProjectViewSet.as_view({
    #     'get':'retrieve',
    #     'put':'update',
    #     'patch':'partial_update',
    #     'dalete':'destroy'
    # })),
    # path('projects/<int:pk>/interfaces/',views.ProjectViewSet.as_view({
    #     'get':'interfaces'
    # })),

    # 7、加载路由条目
    #     方式一：
    #     路由器对象.urls属性可获取生成的路由条目
    # path('',include(router.urls))
]
# 方式二：
# router.urls为列表,将路由条目合并在一个列表中
urlpatterns += router.urls
