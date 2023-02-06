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
        serializer = ProjectSerializer(instance=queryset,many=True)
        # 列表推导式
        # project_list = [{
        #         'id': item.id,
        #         'name': item.name,
        #         'leader': item.leader
        #     } for item in queryset]

        # return JsonResponse(project_list, safe=False)
        return JsonResponse(serializer.data,safe=False)

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

        # 3、创建数据
        # project_obj = Projects.objects.create(name=python_data.get('name'),
        #                                       leader=python_data.get('leader'),
        #                                       is_execute=python_data.get('is_execute'),
        #                                       desc=python_data.get('desc'))
        project_obj = Projects.objects.create(**python_data)

        # 4、将创建成功的数据返回给前端
        python_dict = {
            'id': project_obj.id,
            'name': project_obj.name,
            'msg': '创建成功'
        }
        return JsonResponse(python_dict, status=201)


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
        # 3、将读取的项目数据转化为字典
        # python_data = {
        #     'id': project_obj.id,
        #     'name': project_obj.name,
        #     'msg': '获取数据成功'
        # }
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
        # 4、更新数据
        project_obj.name = python_data.get('name')
        project_obj.is_excute = python_data.get('is_excute')
        project_obj.leader = python_data.get('leader')
        project_obj.desc = python_data.get('desc')
        project_obj.save()

        # 5、将读取的项目数据转化为字典
        python_dict = {
            'id':project_obj.id,
            'name':project_obj.name,
            'msg':'更新项目成功'
        }

        return JsonResponse(python_dict,status=201)

    def delete(self,request,pk):
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

