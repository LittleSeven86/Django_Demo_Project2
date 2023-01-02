import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# 在views
# Create your views here.
# def index(request):
#     return HttpResponse("欢迎测试开发的大佬们")
#
# def get_project(request):
#     return HttpResponse("<h1>获取项目信息</h1>")
#
# def create_project(request):
#     return HttpResponse("<h1>增加项目信息</h1>")
#
# def put_project(request):
#     return HttpResponse("<h1>更新项目信息</h1>")
#
# def delete_project(request):
#     return HttpResponse("<h1>删除项目信息</h1>")
#
# def get_projects(request,pk):
#     return HttpResponse(f"<h1>获取项目{pk}的信息</h1>")
from django.views import View


def get_projects(request):
    '''
    1、视图函数
       -视图函数的第一个参数是HttpRequest对象
       -HttpRequest对象包含了请求的所有数据（请求头、请求体）
       -视图函数必须得返回一个HttpResponse对象或者其子类对象
    '''
    # print(request)
    # print(type(request))
    # print(type(request).__mro__)
    if request.method == 'GET':
        return HttpResponse('<h1>获取项目信息</h1>')
    elif request.method == 'POST':
        return HttpResponse("<h1>创建项目信息</h1>")
    elif request.method == 'PUT':
        return HttpResponse("<h1>更新项目信息</h1>")
    elif request.method == 'DELETE':
        return HttpResponse("<h1>删除项目信息</h1>")
    else:
        return HttpResponse("<h1>其他操作</h1>")


class ProjectsView(View):
    '''
    1、定义类视图
        -必须继承View类或者View子类
        -不同的请求方法有响应的视图函数进行对应
            GET ——> get
            POST ——> post
            PUT ——> put
            delete ——> delete
            PATCH ——>   patch

        -每一个处理请求的方法，必须得返回HttpResponse对象或者HttpResponse子类对象
        -每一个处理请求的方法，第二个参数必须为HttpRequest对象
    '''

    def get(self, request,pk):
        # 创建一个项目信息，本质上还是dict格式
        project_data = {
            'id': 1,
            'name': 'xxxx项目',
            'leader': 'littleseven'
        }
        '''
        HttpResponse
            -HttpResponse第一个参数为字符串类型（需要返回到前端的字符串数据）
            -content_type可以指定响应头中的Content-Type参数
            -status可以指定响应状态码
        使用json.dumps进行转换
        json_str = json.dumps(project_data, ensure_ascii=False，status = 201)
        return HttpResponse(json_str,content_type='application/json')
        内置的转换方法，对HttpResponse进行转换，ensure_ascii=False 将中文不会转换成乱码
        '''
        '''
        JsonResponse
            -为HttpResponse子类
            -用于返回json数据
            -第一个参数可以直接传递字段或者嵌套字典的列表
            -默认添加content_type为application/json
        '''
        return JsonResponse(project_data, json_dumps_params={'ensure_ascii=False'})

    def post(self, request):
        return HttpResponse("<h1>创建项目信息</h1>")

    def put(self, request):
        return HttpResponse("<h1>更新项目信息</h1>")

    def delete(self, request):
        return HttpResponse("<h1>删除项目信息</h1>")
