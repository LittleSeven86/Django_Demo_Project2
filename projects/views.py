import json

from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework import status, filters
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Projects
from projects.serializers import ProjectSerializer, ProjectModelSerializer

# 在views
# Create your views here.


'''
    需求：
    1、获取一条项目数据
      GET /projects/<int:pk>/
    2、获取所有项目数据
      GET /projects/
    3、创建一条项目数据
      POST /projects/    将项目数据以json的形式来传递
    4、更新一条项目数据
      PUT /projects/<int:pk>/   新的项目数据以json的形式来传递
    5、删除一条项目数据
      DELETE /projects/<int:pk>/
'''


# class ProjectsView(View):
# class ProjectsView(APIView):
class ProjectsView(GenericAPIView):
    '''
    2023 0219
    继承GenericAPIView父类（GenericAPIView子类）
        a.具备View的所有特性,
        b.具备了APIView中的认证、授权、限流功能
        还支持对于获取列表数据接口的功能：搜索、排序、分页
    '''
    '''
    继承GenericAPIView后可以优化的代码
        一旦继承GenericAPIView之后，往往需要指定queryset、serializer_class类属性
        queryset指定当前类视图的实例方法需要使用的查询集对象
        serializer_class指定当前类视图的实例方法需要使用的序列化器类
    '''
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer
    # filter_backends在继承了GenericAPIView的类视图中指定使用的过滤引擎类（搜索、排序），过滤优先级高于全局配置settings中过滤引擎类
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    '''
    2、在继承了GenericAPIView的类视图中，search_fields类属性指定模型类中需要进行搜索过滤的字段名
    3、使用icontains查询类型作为过滤类型
    4、可以在字段名称前添加相应符号，指定查询类型
        '^': 'istartswith', 忽略大小写，以..开头
        '=': 'iexact',
        '$': 'iregex',
    '''
    search_fields = ['name', 'leader', 'id']
    '''
    排序
        ordering_fields类属性指定模型类中允许前端进行排序的字段名称
        前端默认可以使用ordering作为排序功能查询字符串参数名称，默认改字段的升序
        如果在字段名称前添加“-”，代表改字段降序
            http://127.0.0.1:8000/projects/?search=小七&ordering=-id
        如果指定多个排序字段，使用英文逗号进行分割
            http://127.0.0.1:8000/projects/?search=小七&ordering=-id,leader
    '''
    ordering_fields = ['id', 'name']

    def get(self, request: Request):
        '''
        2、获取所有项目数据
        GET /projects/
        数据库操作（读取所有项目数据） -> 序列化输出操作（将模型对象转化为Python中的基本类型）

        3、创建一条项目数据
        POST /projects/  新的项目数据以json的形式来传递
        数据校验（规范传入的参数） —> 反序列化输入操作（将json格式的数据转化为复杂的类型） -> 数据库操作（创建项目数据） -> 序列化输出操作（将模型对象转化为Python中的基本类型）
        '''
        # name_param = request.query_params.get('name')
        # if name_param :
        #     queryset = Projects.objects.filter(name__exact= name_param)
        # else:
        #     queryset = Projects.objects.all()
        # 获取所有项目数据（查询集），获取列表数据

        '''
        三、序列化器的使用
            1.可以使用序列化器进行序列化输出操作
            a.创建序列化器对象
            b.可以将模型对象或者查询集对象、普通对象、嵌套普通对象的列表，以instance关键字来传递参数
            c.如果传递的是查询集对象、嵌套普通对象的列表（多条数据），必须得设置many=True
            d.如果传递的是模型对象、普通对象，不需要设置many=True
            e.可以使用序列化器对象的.data属性，获取序列化器之后的数据（字典、嵌套字典的列表）
            '''
        # queryset = Projects.objects.all()
        '''
        2023 0219 
            1、在实例方法中，往往使用get_queryset()方法获取查询集对象
            2、一般不会指定调用queryset类属性，原因：为了提供让用户重写get_queryset()
            3、如果未重写get_queryset()方法，那么必须得指定queryset类属性
        '''
        # queryset = self.get_queryset()
        # filter_queryset对查询对象进行过滤操作
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(instance=page, many=True)
            return self.get_paginated_response(serializer.data)
        '''
            1、在实例方法中，往往使用get_serializer()方法获取序列化器类
            2、一般不会直接调用serializer_class类属性，原因：为了让用户重写get_serializer_class()
            3、如果未重写get_serializer_class()方法，那么必须得指定serializer_class类属性
        '''
        serializer = self.get_serializer(instance=page, many=True)
        '''
        2023 0218 在DRF中Response为HTTPResponse的子类
            a.data参数为序列化之后的数据（一般为字典或嵌套字典的列表）
            b.会自动根据渲染器来将数据转化为请求头中Accept需要的格式进行返回
            c.status指定响应状态码
            d.content_type指定响应头中的Content-Type，一般无需指定，会根据渲染器来自动设置
            e.修改headers,可以直接定义字典，一般无需指定
        '''
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        '''
        2023 0218
        a.一旦继承APIView之后，request是DRF中Request对象
        b.Request是在HttpRequest基础上做了拓展
        c.兼容HttpRequest的所有功能
        d.前端传递的查询字符串参数：GET、query_params
        e.前端传递application/json、application/x-www-form-urlencoded、multipart/form-data参数,可以根据请求头中Content-Type，使用统一的data属性获取
        '''

        '''
        四、反序列化操作
        1.定义序列化器类，使用data关键字参数传递字典参数
        2.可以使用序列化器对象调用.is_valid()方法，才会开始对前端输入的参数进行校验
        3.如果校验通过.is_valid()方法返回True，否则返回False
        4.如果调用.is_valid()方法，添加raise_exeception=True，校验不通过会抛出异常，否则不会抛出异常
        5.只有在调用.is_valid()方法之后，才可以使用序列化器对象调用.errors属性，来获取错误提示信息（字典类型）
        6.只有在调用.is_valid()方法之后，才可以使用序列化器对象调用.validated_data属性，来获取校验通过之后的数据，与使用json.load转化之后的数据有区别
        '''
        '''
        2023 0215
            1、如果在创建序列化器对象时，仅传递data参数，使用序列化器对象调用save方法时，会自动调用序列化器类中的create方法
            2、create方法用于对数据进行创建操作
            3、序列化器类中的create方法，validated_data参数为校验通过之后的数据（一般字典类型）
            4、在调用save方法时，可以传递任意的关键字参数，并且会自动合并到validated_data字典中
            5、create方法一般需要将创建成功之后模型对象返回
        '''
        serializer11 = self.get_serializer(data=request.data)
        serializer11.is_valid(raise_exception=True)

        # 3、创建数据
        project_obj = serializer11.save()

        # 4、将创建成功的数据返回给前端
        '''
        2023 0215
            1、在创建序列化器对象时，仅仅只传递data参数，那么必须得调用is_valid()方法通过之后
            2、如果没有调用save方法，使用创建序列化器对象.data属性，来获取序列化输出的数据
              （会把validated_data数据作为输入源，参照序列化器字段的定义来进行输入）
            3、如果调用了save方法，使用创建序列化器对象.data属性，来获取序列化输出的数据
              （会把create方法返回的模型对象数据作为输入源，参照序列化器字段的定义来进行输出）
        '''
        return Response(serializer11.data, status=status.HTTP_201_CREATED)


class ProjectsDetailView(GenericAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer

    '''
        a.lookup_url_kwarg默认为None
        b.如果lookup_url_kwarg为None，那么lookup_url_kwarg与lookup_field值相同（‘pk’）
        c.lookup_url_kwarg指定url路由条目中外键的路径参数名称，一般无需指定
    '''
    # lookup_url_kwarg = 'kk'
    """
       1、获取一条项目数据（获取详情数据）
           GET /projects/<int:pk>/
           数据校验（规范传入的参数） -> 数据库操作（读取一条项目数据） -> 序列化输出操作（将模型对象转化为Python中的基本类型）

       4、更新一条项目数据
           PUT /projects/<int:pk>/   新的项目数据以json的形式来传递
           数据校验（规范传入的参数） —> 反序列化输入操作（将json格式的数据转化为复杂的类型） -> 数据库操作（更新项目数据）-> 序列化输出操作（将模型对象转化为Python中的基本类型）

       5、删除一条项目数据
           DELETE /projects/<int:pk>/
           数据校验（规范传入的参数） -> 数据库操作（删除一条项目数据）
       """

    # def get_object(self,pk):
    #     try:
    #         project_obj = self.get_queryset().get(id__exact=pk)
    #         return project_obj
    #     except Exception as e:
    #         return Response({'msg': '参数有误'}, status=400)

    def get(self, request, pk):
        '''
        1、需要校验pk在数据库中是否存在
        2、从数据库中读取项目数据
        '''
        # try:
        #     project_obj = Projects.objects.get(id__exact=pk)
        # except Exception as e:
        #     return JsonResponse({'msg': '参数有误'}, status=400)
        # get_object可以获取模型对象，无需传递外键值
        project_obj = self.get_object()
        serializer = self.get_serializer(instance=project_obj)
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        '''
        1、需要校验pk在数据库中是否存在
        2、从数据库中读取项目数据
        '''
        project_obj = self.get_object()

        '''
        2023 0215
            1、如果在创建序列化器对象时，同时instance和data参数，使用序列化器对象调用save方法时，会自动调用序列化器类中的update方法
            2、update方法用于对数据进行更新操作
            3、序列化器类中的update方法，instance参数为待更新的模型对象，validated_data参数为校验通过之后的数据（一般字典类型）
            4、在调用save方法时，可以传递任意的关键字参数，并且会自动合并到validated_data字典中
            5、update方法一般需要将更新成功之后模型对象返回
        '''
        serializer = self.get_serializer(instance=project_obj, data=request.data)

        # if not serializer.is_valid():
        #     return JsonResponse(serializer.errors, status=401)
        # 在序列化器对象调用is_valid(raise_exception=True)，校验失败时，会抛出异常，DRF框架会自动处理异常
        serializer.is_valid(raise_exception=True)

        # 4、更新数据
        serializer.save()

        # 5、将读取的项目数据转化为字典
        serializer = self.serializer_class(instance=project_obj)
        return JsonResponse(serializer.data, status=201)

    def delete(self, request, pk):
        '''
        1、需要校验pk在数据库中是否存在
        2、读取主键为pk的项目数据
        '''
        # try:
        #     project_obj = self.get_object(id=pk)
        # except Exception as e:
        #     return JsonResponse({'msg': '参数有误'}, status=400)
        project_obj = self.get_object()
        # 3、执行删除
        project_obj.delete()
        return JsonResponse({'msg': '删除成功'}, status=204)
