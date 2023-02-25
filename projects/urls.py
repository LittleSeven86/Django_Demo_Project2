#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :urls.py
# @Time      :2023/1/2 11:07
# @Author    :LittleSeven
# @Address   ：https://github.com/MengZhang893/Demo1_1.git

from django.urls import path
from projects import views
from . import views


urlpatterns = [
    # path('get/', views.get_project),
    # path('create/',views.create_project),
    # path('put/', views.put_project),
    # path('delete/',views.delete_project)
    # 定义类试图的路由条目
    # 类型图.as_view() 进行调用
    # path('projects/',views.ProjectsView.as_view()),
    path('projects/',views.ProjectViewSet.as_view({
        'get':'list',
        'post':'create'
    })),
    # path('projects/<int:pk>/',views.ProjectsDetailView.as_view()),
    path('projects/<int:pk>/',views.ProjectViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'patch':'partial_update',
        'dalete':'destroy'
    })),

]