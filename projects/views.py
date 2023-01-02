from django.http import HttpResponse
from django.shortcuts import render

#在views
# Create your views here.
def index(request):
    return HttpResponse("欢迎测试开发的大佬们")

def get_project(request):
    return HttpResponse("<h1>获取项目信息</h1>")

def create_project(request):
    return HttpResponse("<h1>增加项目信息</h1>")

def put_project(request):
    return HttpResponse("<h1>更新项目信息</h1>")

def delete_project(request):
    return HttpResponse("<h1>删除项目信息</h1>")