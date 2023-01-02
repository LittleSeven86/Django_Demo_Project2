#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :urls.py
# @Time      :2023/1/2 11:07
# @Author    :LittleSeven
# @Address   ：https://github.com/MengZhang893/Demo1_1.git
from importlib.resources import path
from projects import views

urlpatterns = [
    path('get/', views.get_project),
    path('create/',views.create_project),
    path('put/',views.put_project),
    path('delete/',views.delete_project)
]