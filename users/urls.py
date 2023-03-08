#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
-----------------------------------------------------------
    @FileName  :urls.py
    @Time      :2023/3/6 21:41
    @Author    :LittleSeven
    @Address   ：https://gitee.com/linguchong/Demo1_1.git
-----------------------------------------------------------
'''

from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from . import views

# router = routers.SimpleRouter()
# router.register(r'users', views.UserView)

urlpatterns = [
    # path('user/register/', views.UserView.as_view()),
    path('register/', views.UserView.as_view({'post': 'create'})),
    re_path(r'^(?P<username>\w{6,20})/count/$', views.UsernameIsExistedView.as_view()),
    re_path(r'^(?P<email>[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+)/count/$',
            views.EmailIsExistedView.as_view()),
    path('login/', obtain_jwt_token),
]

# 方式二：
# router.urls为列表
# urlpatterns += router.urls
