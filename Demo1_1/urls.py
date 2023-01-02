"""Demo1_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from projects import views
from projects import urls

'''
一、什么是路由？
    1、定义
        指的是url和后端视图之间的一一映射关系
        
    2、添加
        需要在全局路由文件中（urls.py），urlpatterns列表中添加路由条目
        urlpatterns列表条目数就是路由总数
        urlpatterns列表从上到下进行匹配（路由寻址）
        urlpatterns列表中条目一旦匹配成功，就会终止向下匹配，不成功就会一直向下匹配，全部不成功会抛出404
        
    3、path函数
        用于定义路由条目
        第一个参数位URL路径参数，为String，路径前不能添加/，路径最后需要添加/
        第二个参数为视图函数活着类视图，如果添加的视图函数，无须使用()调用
        如果第二个参数为include，那么会继续进入到子路由中匹配，子路由的匹配规则与全局路由一致
        
        
'''


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/',views.index),
    # path('get_projects/',views.get_projects),
    # path('get_projects/1',views.get_projects1),
    path('get_projects/2',views.get_projects2),
    path('project/',include('projects.urls'))
]
