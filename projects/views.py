import json,logging

from django.http import JsonResponse
from rest_framework import status, filters
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser

from .models import Projects
from projects.serializers import ProjectSerializer, ProjectModelSerializer,ProjectNamesModelSerializer
from utils.pagination import PageNumberPagination



logger = logging.getLogger('Demo1_1')

# 在views
# Create your views here.
# Mixin拓展类

# class ListCreateAPIView(
#     mixins.CreateModelMixin,
#     mixins.ListModelMixin,
#     GenericAPIView):
#     def get(self, request: Request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ProjectsView(View):
# class ProjectsView(APIView):
class ProjectsView(generics.ListCreateAPIView):
    """
   a.直接继承Mixin拓展类，拓展类只提供了action方法
   b.action方法有哪些呢？
       list            --> 获取列表数据
       retrieve        --> 获取详情数据
       create          --> 创建数据
       update          --> 更新数据（完整）
       partial_update  --> 更新数据（部分）
       destroy         --> 删除数据
   c.类视图往往只能识别如下方法？
       get   -->  list
       get   -->  retrieve
       post  -->  create
       put   -->  update
       patch -->  partial_update
       delete -->  destroy
   d.为了进一步优化代码，需要使用具体的通用视图XXXAPIView
       """
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer
    # filter_backends在继承了GenericAPIView的类视图中指定使用的过滤引擎类（搜索、排序），过滤优先级高于全局配置settings中过滤引擎类
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'leader', 'id']
    ordering_fields = ['id', 'name']
    # 可以在类视图中指定分页引擎类，优先级高于全局
    pagination_class = PageNumberPagination

    # def get(self, request: Request,*args,**kwargs):
    #     # queryset = self.filter_queryset(self.get_queryset())
    #     # page = self.paginate_queryset(queryset)
    #     # if page is not None:
    #     #     serializer = self.get_serializer(instance=page, many=True)
    #     #     # 4、调用get_paginated_response方法，将序列化之后的数据进行分页，并返回Response响应
    #     #     return self.get_paginated_response(serializer.data)
    #     # serializer = self.get_serializer(instance=page, many=True)
    #     # return Response(serializer.data, status=status.HTTP_200_OK)
    #     '''
    #     a.python中支持多重继承，一个类可以同时继承多个父类
    #     b.类中的方法和属性是按照__mro__所指定的继承顺序进行搜索
    #     '''
    #     print(ProjectsView.__mro__)
    #     return self.list(request,*args,**kwargs)
    #
    # def post(self, request,*args,**kwargs):
    #     # serializer11 = self.get_serializer(data=request.data)
    #     # serializer11.is_valid(raise_exception=True)
    #     # # 3、创建数据
    #     # serializer11.save()
    #     # return Response(serializer11.data, status=status.HTTP_201_CREATED)
    #     return self.create(request,*args,**kwargs)


# class ProjectsDetailView(
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     GenericAPIView):
class ProjectsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer

    def get(self, request, *args,**kwargs):
        '''
        1、需要校验pk在数据库中是否存在
        2、从数据库中读取项目数据
        '''
        # project_obj = self.get_object()
        # serializer = self.get_serializer(instance=project_obj)
        # return JsonResponse(serializer.data)
        return self.retrieve(request, *args,**kwargs)

    def put(self, request, *args,**kwargs):
        '''
        1、需要校验pk在数据库中是否存在
        2、从数据库中读取项目数据
        '''
        # project_obj = self.get_object()
        #
        # serializer = self.get_serializer(instance=project_obj, data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # serializer = self.serializer_class(instance=project_obj)
        # return JsonResponse(serializer.data, status=201)
        return self.update(request, *args,**kwargs)

    def delete(self, request, *args,**kwargs):
        '''
        1、需要校验pk在数据库中是否存在
        2、读取主键为pk的项目数据
        '''
        # project_obj = self.get_object()
        # # 3、执行删除
        # project_obj.delete()
        # return JsonResponse({'msg': '删除成功'}, status=204)
        return self.destroy(request, *args,**kwargs)

'''
视图集
    a.可以继承视图集父类ViewSet
    b.在定义url路由条目时，支持给as_view传递字典参数（请求方法名与具体调用的action方法名的一一对应关系）
    c.ViewSet继承了ViewSetMixin, views.APIView
    d.具备APIView的所有功能
    e.继承ViewSetMixin，所有具备传给as_view传递字典参数（请求方法名与具体调用的action方法名的一一对应关系）
'''
# class ProjectViewSet(viewsets.ModelViewSet):
# class ProjectViewSet(
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.CreateModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     viewsets.GenericViewSet):

'''
a.ModelViewSet是一个最完整的视图集类
b.提供了获取列表数据接口、获取详情数据接口、创建数据接口、更新数据接口、删除数据的接口
c.如果需要对某个模型进行增删改查操作，才会选择ModelViewSet
d.如果仅仅只对某个模型进行数据读取操作（取列表数据接口、获取详情数据接口），一般会选择ReadOnlyModelViewSet
'''
class ProjectViewSet(viewsets.ModelViewSet):
    """
    list:
    获取项目列表数据

    retrieve:
    获取项目详情数据

    update:
    更新项目数据

    names:
    获取项目名称

    """

    # def list(self, request, *args, **kwargs):
    #     pass
    #
    # def retrieve(self, request, *args, **kwargs):
    #     pass
    #
    # def create(self, request, *args, **kwargs):
    #     pass
    #
    # def update(self, request, *args, **kwargs):
    #     pass
    #
    # def partial_update(self, request, *args, **kwargs):
    #     pass
    #
    # def destroy(self, request, *args, **kwargs):
    #     pass
    parser_classes = [JSONParser]
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'leader', 'id']
    ordering_fields = ['id', 'name']
    # # 可以在类视图中指定分页引擎类，优先级高于全局
    # pagination_class = PageNumberPagination
    # # 在继承了APIView的类视图中，可以使用permission_classes类属性指定权限类，值为列表，可添加多个权限类
    # permission_classes = [permissions.IsAuthenticated]

    # 在继承了APIView的类视图中，可以使用authentication_classes类属性指定认证类，值为列表，可添加多个认证类
    # 优秀级高于全局，一般无需在特定类视图中指定
    # authentication_classes = []
    '''
    1、如果需要使用路由器机制自动生成路由条目，那么就必须得使用action装饰器
    2、methods指定需要使用的请求方法，如果不指定，默认为GET
    3、detail指定是否为详情接口，是否需要传递当前模型的pk值,
      -如果需要传递当前模型的pk值，那么detail=True，否则detail=False
    4、url_path指定url路径，默认为action方法名称
    5、url_name指定url路由条目名称后缀，默认为action方法名称
    @action(methods=['GET'], detail=False, url_path='xxx', url_name='yyyy')
    '''
    # @action(methods=['GET'],detail=False,url_path='xxx',url_name='yyy')
    @action(methods=['GET'],detail=False,)
    def names(self,request,*args,**kwargs):
        # queryset = self.get_queryset()
        queryset = self.filter_queryset(self.get_queryset())
        # name_list = []
        # for project in queryset:
        #     name_list.append({
        #         'id':project.id,
        #         'name':project.name
        #     })
        serializer = self.get_serializer(queryset,many = True)

        # return Response(serializer.data,status=200)
        response = super().list(request,*args,**kwargs)
        logger.info(response.data)
        return response
    
    @action(detail=True)
    def interfaces(self,requeset,*args,**kwargs):
        project = self.get_object()
        interfaces_qs = project.interfaces_set.all()
        interfaces_data = [{'id': interface.id, 'name': interface.name} for interface in interfaces_qs]

        logger.debug(interfaces_data)
        return Response(interfaces_data,status=200)

    def get_serializer_class(self):
        '''
        a.可以重写父类的get_serializer_class方法，用于为不同的action提供不一样的序列化器类
        b.在视图集对象中可以使用action属性获取当前访问的action方法名称
        '''
        # print(ProjectModelSerializer.__mro__)
        if self.action == 'names':
            return ProjectNamesModelSerializer
        else:
            return super().get_serializer_class()

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        response.data.pop('id')
        response.data.pop('create_time')
        return response

    # def filter_queryset(self, queryset):
    #     if self.action =='names':
    #         return self.queryset
    #     else:
    #         return super().filter_queryset(queryset)

    def paginator_queryset(self,queryset):
        if self.action =='names':
            return
        else:
            return super().paginate_queryset(queryset)

    def get_queryset(self):
        if self.action =='names':
            return self.queryset.filter(name__icontains='2')
        else:
            return super().get_queryset()

'''
如何定义类视图？类视图的设计原则？
    a.类视图尽量要简单
    b.根据需求选择相应的父类视图
    c.如果DRF中的类视图有提供相应的逻辑，那么就直接使用父类提供的
    d.如果DRF中的类视图，绝大多数逻辑都能满足需求，可以重写父类实现
    e.如果DRF中的类视图完全不满足要求，那么就直接自定义即可
'''

'''
认证与授权
1、认证：获取权限的方式
2、授权：通过认证之后，可以获取哪些特权
'''