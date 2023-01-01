from django.http import HttpResponse
from django.shortcuts import render

#在views
# Create your views here.
def index(request):
    return HttpResponse("欢迎测试开发的大佬们")

def get_projects(request):
    return HttpResponse("<h1>这是一个项目信息</h1>")

def get_projects1(request):
    return HttpResponse("<h1>这是一个项目信息1</h1>")

def get_projects2(request):
    return HttpResponse("<h1>这是一个项目信息2</h1>")