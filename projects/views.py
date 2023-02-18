import json

from django.http import HttpResponse, JsonResponse
from django.views import View

from .models import Projects
from projects.serializers import ProjectSerializer

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


class ProjectsView(View):

    def get(self, request):
        '''
        2、获取所有项目数据
        GET /projects/
        数据库操作（读取所有项目数据） -> 序列化输出操作（将模型对象转化为Python中的基本类型）

        3、创建一条项目数据
        POST /projects/  新的项目数据以json的形式来传递
        数据校验（规范传入的参数） —> 反序列化输入操作（将json格式的数据转化为复杂的类型） -> 数据库操作（创建项目数据） -> 序列化输出操作（将模型对象转化为Python中的基本类型）
        '''
        # 获取所有项目数据（查询集），获取列表数据
        queryset = Projects.objects.all()

        # b.将项目的查询集数据转化为嵌套字典的列表
        # project_list = []
        # for item in queryset:
        #     item: Projects
        #     # project_dict = {
        #     #     'id':item.id,
        #     #     'name':item.name,
        #     #     'leader':item.leader
        #     # }
        #     project_list.append({
        #         'id': item.id,
        #         'name': item.name,
        #         'leader': item.leader
        #     })
        '''
        三、序列化器的使用
            1.可以使用序列化器进行序列化输出操作
            a.创建序列化器对象
            b.可以将模型对象或者查询集对象、普通对象、嵌套普通对象的列表，以instance关键字来传递参数
            c.如果传递的是查询集对象、嵌套普通对象的列表（多条数据），必须得设置many=True
            d.如果传递的是模型对象、普通对象，不需要设置many=True
            e.可以使用序列化器对象的.data属性，获取序列化器之后的数据（字典、嵌套字典的列表）
            '''
        serializer = ProjectSerializer(instance=queryset, many=True)
        # 列表推导式
        # project_list = [{
        #         'id': item.id,
        #         'name': item.name,
        #         'leader': item.leader
        #     } for item in queryset]

        # return JsonResponse(project_list, safe=False)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        '''
        1、获取json参数并转化为python中的数据类型（字典）

        2、需要进行大量的数据校验（非常麻烦）
          a.需要校验必传参数是否有传递
          b.传递的有唯一约束的参数是否已经存在
          c.必传参数的长度是否超过限制
          d.校验传参类型

         3、创建数据

         4、将创建成功的数据返回给前端
        '''
        try:
            python_data = json.loads(request.body)
        except Exception as e:
            return JsonResponse({'msg': '参数有误'}, status=400)

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
        serializer11 = ProjectSerializer(data=python_data)
        if not serializer11.is_valid(raise_exception=False):
            return JsonResponse(serializer11.errors, status=401)

        # 3、创建数据
        # project_obj = serializer11.save(myname = 'lisa',age = 18)
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
        return JsonResponse(serializer11.data, status=201)


class ProjectsDetailView(View):
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

    def get(self, request, pk):
        '''
        1、需要校验pk在数据库中是否存在
        2、从数据库中读取项目数据
        '''
        try:
            project_obj = Projects.objects.get(id__exact=pk)
        except Exception as e:
            return JsonResponse({'msg': '参数有误'}, status=400)
        serializer = ProjectSerializer(instance=project_obj)
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        '''
        1、需要校验pk在数据库中是否存在
        2、从数据库中读取项目数据
        '''
        try:
            project_obj = Projects.objects.get(id__exact=pk)
        except Exception as e:
            return JsonResponse({'msg': '数据有误'}, status=400)
        # 3、获取json参数并转化为python中的数据类型（字典）
        try:
            python_data = json.loads(request.body)
        except Exception as e:
            return JsonResponse({'msg': '参数有误'}, status=400)

        # 需要进行大量的数据校验，且非常复杂
        # serializer11 = ProjectSerializer(data=python_data)
        '''
        2023 0215
            1、如果在创建序列化器对象时，同时instance和data参数，使用序列化器对象调用save方法时，会自动调用序列化器类中的update方法
            2、update方法用于对数据进行更新操作
            3、序列化器类中的update方法，instance参数为待更新的模型对象，validated_data参数为校验通过之后的数据（一般字典类型）
            4、在调用save方法时，可以传递任意的关键字参数，并且会自动合并到validated_data字典中
            5、update方法一般需要将更新成功之后模型对象返回
        '''
        serializer = ProjectSerializer(instance=project_obj, data=python_data)

        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=401)

        # 4、更新数据
        # project_obj.save()
        serializer.save()

        # 5、将读取的项目数据转化为字典
        serializer = ProjectSerializer(instance=project_obj)
        return JsonResponse(serializer.data, status=201)

    def delete(self, request, pk):
        '''
        1、需要校验pk在数据库中是否存在
        2、读取主键为pk的项目数据
        '''
        try:
            project_obj = Projects.objects.get(id=pk)
        except Exception as e:
            return JsonResponse({'msg': '参数有误'}, status=400)

        # 3、执行删除
        project_obj.delete()
        return JsonResponse({'msg': '删除成功'}, status=204)
