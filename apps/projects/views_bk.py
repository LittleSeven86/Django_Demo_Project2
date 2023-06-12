import json

from django.http import JsonResponse
from rest_framework import status, filters
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Projects
from projects.serializers import ProjectSerializer, ProjectModelSerializer
from utils.pagination import PageNumberPagination

# 在views
# Create your views here.
# Mixin拓展类
class ListModelMixin:
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # 3、调用paginate_queryset方法对查询集对象进行分页
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(instance=page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(instance=queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateModelMixin:
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# class ProjectsView(View):
# class ProjectsView(APIView):
class ProjectsView(CreateModelMixin,ListModelMixin,GenericAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer
    # filter_backends在继承了GenericAPIView的类视图中指定使用的过滤引擎类（搜索、排序），过滤优先级高于全局配置settings中过滤引擎类
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'leader', 'id']
    ordering_fields = ['id', 'name']
    # 可以在类视图中指定分页引擎类，优先级高于全局
    pagination_class = PageNumberPagination

    def get(self, request: Request,*args,**kwargs):
        # queryset = self.filter_queryset(self.get_queryset())
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(instance=page, many=True)
        #     # 4、调用get_paginated_response方法，将序列化之后的数据进行分页，并返回Response响应
        #     return self.get_paginated_response(serializer.data)
        # serializer = self.get_serializer(instance=page, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)
        '''
        a.python中支持多重继承，一个类可以同时继承多个父类
        b.类中的方法和属性是按照__mro__所指定的继承顺序进行搜索
        '''
        print(ProjectsView.__mro__)
        return self.list(request,*args,**kwargs)

    def post(self, request,*args,**kwargs):
        # serializer11 = self.get_serializer(data=request.data)
        # serializer11.is_valid(raise_exception=True)
        # # 3、创建数据
        # serializer11.save()
        # return Response(serializer11.data, status=status.HTTP_201_CREATED)
        return self.create(request,*args,**kwargs)


class ProjectsDetailView(GenericAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer

    def get(self, request, pk):
        '''
        1、需要校验pk在数据库中是否存在
        2、从数据库中读取项目数据
        '''
        project_obj = self.get_object()
        serializer = self.get_serializer(instance=project_obj)
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        '''
        1、需要校验pk在数据库中是否存在
        2、从数据库中读取项目数据
        '''
        project_obj = self.get_object()

        serializer = self.get_serializer(instance=project_obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer = self.serializer_class(instance=project_obj)
        return JsonResponse(serializer.data, status=201)

    def delete(self, request, pk):
        '''
        1、需要校验pk在数据库中是否存在
        2、读取主键为pk的项目数据
        '''
        project_obj = self.get_object()
        # 3、执行删除
        project_obj.delete()
        return JsonResponse({'msg': '删除成功'}, status=204)
