from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):

    return HttpResponse("欢迎测试开发的大佬们")