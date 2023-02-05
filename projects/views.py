import json

from django.db.models import Count, Q, Sum
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db import connection

from interfaces.models import Interfaces
from .models import Projects

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


# class ProjectsView(View):
#     '''
#     1、定义类视图
#         -必须继承View类或者View子类
#         -不同的请求方法有响应的视图函数进行对应
#             GET ——> get
#             POST ——> post
#             PUT ——> put
#             delete ——> delete
#             PATCH ——>   patch
#
#         -每一个处理请求的方法，必须得返回HttpResponse对象或者HttpResponse子类对象
#         -每一个处理请求的方法，第二个参数必须为HttpRequest对象
#     '''
#
#     # def get(self, request, pk):
#     #     # 创建一个项目信息，本质上还是dict格式
#     #     project_data = {
#     #         'id': 1,
#     #         'name': 'xxxx项目',
#     #         'leader': 'littleseven'
#     #     }
#
#     #     HttpResponse
#     #         -HttpResponse第一个参数为字符串类型（需要返回到前端的字符串数据）
#     #         -content_type可以指定响应头中的Content-Type参数
#     #         -status可以指定响应状态码
#     #      使用json.dumps进行转换,内置的转换方法，对HttpResponse进行转换，ensure_ascii=False 将中文不会转换成乱码
#     # json_str = json.dumps(project_data, ensure_ascii=False,)
#     # print(json_str)
#     # return HttpResponse(json_str, content_type='application/json',status=301)
#     #
#     # project_data_list = [
#     #     {
#     #         'id': 1,
#     #         'name': 'xxxx项目',
#     #         'leader': 'littleseven'
#     #     },
#     #     {
#     #         'id': 2,
#     #         'name': 'yyyy项目',
#     #         'leader': 'littleseven'
#     #     },
#     #     {
#     #         'id': 3,
#     #         'name': 'zzzz项目',
#     #         'leader': 'littleseven'
#     #     }
#     # ]
#     # return JsonResponse(project_data_list, json_dumps_params={'ensure_ascii': False}, safe=False)
#
#     #     '''
#     #     JsonResponse
#     #         -为HttpResponse子类
#     #         -用于返回json数据
#     #         -第一个参数可以直接传递字段或者嵌套字典的列表
#     #         -默认添加content_type为application/json
#     #         -默认第一个参数只能为字典，如果为嵌套字典的列表，需要设置safe为False
#     #     '''
#     #     '''
#     #     两种开发模式：
#     #         -前后端不分离的开发模式
#     #             -后端如果返回的是一个HTML页面（页面中有填充数据）
#     #             -后段需控制数据的展示
#     #             -前后端不分家，耦合严重
#     #             -返回的是HTML页面，实用性差，适配做得比较差
#     #
#     #         -前后端分离的开发模式
#     #             -后端如果返回的是数据（json、xml）
#     #             -当前主流，后端只对数据进行处理，只提供数据
#     #             -前端效率、页面好不好看，全由前端负责，前后端完全独立
#     #             -前端发送给json格式，后端返回json，适用性好、拓展性好，适配性好
#     #     '''
#
#     def get(self, request, pk):
#         '''
#         1、创建
#             -方式一：
#             -直接使用模型类(字段名1=值1,字段名1=值1,....)，来创建模型类实例
#             -必须使用模型对象/模型实例调用save方法才会执行SQL语句
#         '''
#         # obj = Projects(name='xxx金融项目', leader='xxx负责人', )
#         # obj.save()
#         # pass
#         '''
#             -方式二
#             -使用模型类.objects返回manage对象
#             -manage对象.create(字段名1=值1,字段名1=值1,....)，来创建模型类实例
#             -无须使用模型对象/模型实例调用save方法，会自动执行SQL语句
#
#         '''
#         # obj = Projects.objects.create(name='xxx222', leader='lemon', )
#         # pass
#         # return JsonResponse(project_data_list, json_dumps_params={'ensure_ascii': False}, safe=False)
#
#         '''
#         2、读取数据
#             2.1 读取多条数据
#                 -读取数据库中所有的数据
#                 -可以使用模型类.objects.all()，会将当前模型类对应的数据表中的所有数据读取出来
#                 -模型类.objects.all()，返回QuerySet(查询集对象)
#                 -QuerySet对象，类似于列表，具有惰性查询的特性('在用数据的时候，才会执行sql语句')
#         '''
#         # qs = Projects.objects.all()
#         # pass
#
#         # 聚合运算
#         # qs = Projects.objects.filter(name__contains='222').aggregate(Count('id'))
#         # pass
#
#         # 分组运算
#         # qs = Projects.objects.values('id').annotate(Count('interfaces'))
#         # pass
#         '''
#             2.2 读取单条数据
#                 -方式一：
#                 -可以使用模型类.objects.get(条件1=值1,。。。)
#                 -如果使用指定条件查询结果记录数量=0，会抛出{DoesNotExist}Projects matching query does not exist.异常
#                 -如果使用指定条件查询结果记录数量>1，{MultipleObjectsReturned}get() returned more than one Projects -- it returned 3!
#                 -最好使用具有唯一约束的条件去查询
#                 -如果使用指定条件查询结果记录数量=1，会返回这条记录对应的模型实例对象，可以使用模型对象.字段名去获取响应的字段值
#         '''
#         # obj = Projects.objects.get(id = 5)
#         #
#         # pass
#
#         '''
#         -方式二：
#         -可以使用模型类.objects.filter(条件1=值1,。。。)
#         -如果使用指定条件查询结果记录数量=0，会返回空的QuerySet对象
#         -如果使用指定条件查询结果记录数量>1，将符合条件的模型对象，包裹到QuerySet对象中返回
#         -QuerySet对象，类似于列表，有如下特性：
#             -支持通过数值(正整数)索引取值
#             -支持切片操作(正整数)
#             -获取第一个元素：QuerySet对象.first()
#             -获取长度：len()函数，QuerySet对象.count()查询
#             -判断查询集是否为空:QuerySet对象.exists()
#             -支持迭代操作(for循环，每次循环返回模型对象)
#         '''
#         # qs = Projects.objects.filter(id = 5)
#         # pass
#         '''
#         ORM框架中，会给每一个模型类中的主键设置一个别名（pk）
#         filter方法支持多种查询类型
#             1）字段名__查询类型=具体值
#             2）字段名__exact=具体值，缩写形式为：字段名=具体值
#             3）字段名__gt：大于、字段名__gte：大于等于
#             4）字段名__lt：小于、字段名_lte：小于等于
#             5）contains：包含
#             6）startswith：以xxx开头
#             7）endswith：以xxx结尾
#             8）isnull：是否为null
#             9）一般在查询类型前添加“i”，代表忽略大小写
#
#         exclude为反向查询，filter方法支持的所有查询类型，都支持
#         '''
#         # qs = Projects.objects.exclude(id= 5)
#         # pass
#
#         '''
#         创建从表数据
#         外键对应的父表如何传递？
#         方式一:
#             1）先获取父表模型对象,查询到
#             2）从表主键用获取的父表模型对象和外键字段名作为参数来传递
#         '''
#         # project_obj = Projects.objects.get(name='在线图书项目')
#         # interface_obj = Interfaces.objects.create(name='在线图书项目-注册接口',tester='小七',projects=project_obj)
#         # pass
#         '''
#         方式二：
#             1）先获取父表模型对象，进而获取父表数据的id值
#             2）将父表数据的主键id值以外键名_id作为参数来传递
#         '''
#         # interface_obj = Interfaces.objects.create(name='在线图书项目-更新接口', tester='小八', projects_id=project_obj.id)
#         # pass
#         '''
#         a.通过从表模型对象（已经获取到了），如何获取父表数据？
#             -可以通过从表外键字段先获取父表模型对象
#             -interface_obj.projects，返回父表模型对象
#         '''
#         # interface_obj = Interfaces.objects.get(id__exact= 1)
#         # interface_obj.projects
#         # pass
#         '''
#         b.通过父表模型对象（已经获取到了），如何获取从表数据？
#           django 默认每个主表的对象都有一个是外键的属性，可以通过它来查询到所有属于主表的子表的信息。
#           默认可以通过父表模型对象.从表模型类名小写_set，返回manager对象，可以进一步使用filter进行过滤
#           如果在从表模型类的外键字段指定了related_name参数，那么会使用related_name指定参数作为名称
#           project_obj.interfaces_set.all()
#
#           在实际项目中，我们使用最多的还是related_name
#           如果你觉得上面的定义比较麻烦的话，你也可以在定义主表的外键的时候，给这个外键定义好一个名称。要用related_name比如在Interfacees表中：
#           projects = models.ForeignKey('projects.Projects', on_delete=models.CASCADE,verbose_name='所属项目', help_text='所属项目',related_name = 'project_interface')
#           那么实现以上的需求，就可以使用projects.interfaces_set.all()
#           也可以使用project.project_interface.all()
#         '''
#         # project_obj = Projects.objects.get(id__exact=5)
#         # project_obj.interfaces_set.all()
#         # pass
#
#         '''
#         如果想要通过父表参数来获取从表数据、想要通过从表参数获取父表数据  --- 关联查询
#         可以使用关联查询语句：
#         关联字段名称__关联模型类中的字段名称__查询类型
#         '''
#         # Projects.objects.filter(interfaces__name__iexact='在线图书项目-登录接口')
#         # Interfaces.objects.filter(projects__id__gt= 3)
#         # pass
#
#         '''
#         逻辑查询
#         与关系
#         方式一：
#           在同一个filter方法内部，添加多个关键字参数，那么每个条件为“与”的关系
#         方式二：
#           可以多次调用filter方法，那么filter方法的条件为“与”的关系  --- QuerySet链式调用特性
#         '''
#         # qs = Projects.objects.filter(name__contains='22',leader='lemon')
#         # qs1 = Projects.objects.filter(name__contains='xxx').filter(leader='lemon')
#         # pass
#
#         '''
#         或关系
#           可以使可以使用Q查询，实现逻辑关系，多个Q对象之间如果使用“|”，那么为“或”关系
#         '''
#         # qs = Projects.objects.filter(Q(name__contains='xxx')|Q(leader='lemon'))
#         # pass
#
#         '''
#         排序（QuerySet）
#             可以使用QuerySet对象（manager对象）.order_by('字段名1', '字段名2', '-字段名3')
#             默认为ASC升序，可以在字段名称前添加“-”，那么为DESC降序
#         '''
#         # Projects.objects.filter(Q(name__contains='xxx')|Q(leader='lemon')).order_by('name')
#         # pass
#
#         '''
#         三、更新（U）
#         方式一：一条数据
#             1）必须调用save方法才会执行sql语句，并且默认进行完整更新
#             2）可以在save方法中设置update_fields参数（序列类型），指定需要更新的字段名称（字符串），将指定字段存入列表中
#         '''
#         # project_obj = Projects.objects.get(id__exact=5)
#         # project_obj.name = '在线图书项目（一期）'
#         # project_obj.leader = '小七'
#         # project_obj.save(update_fields=['name','leader'])
#
#         '''
#         方式二：多条数据
#             可以在QuerySet对象.update(字段名称='字段值')，返回修改成功的值，无需调用save方法
#         '''
#         # qs = Projects.objects.filter(name__contains='x').update(leader = '老八')
#         # pass
#
#         '''
#         四、删除（D）
#         删除一条数据
#             先获取到模型对象，然后调用delete方法进行删除
#
#         删除多条数据
#             先获取查询集，然后调用delete方法进行删除
#
#         '''
#         # project_obj = Projects.objects.get(id__exact=10).delete()
#         # pass
#         #
#         # project_obj = Projects.objects.filter(name__contains='xx').delete()
#         # pass
#
#         '''
#         聚合运算
#             -可以使用QuerySet对象.aggregate(聚合函数('字段名'))方法，返回字典数据
#             -返回的字典数据中key为字段名__聚合函数名小写
#             -可以使用关键字参数形式，那么返回的字典数据中key为关键字参数名
#         '''
#         # qs = Projects.objects.filter(name__contains='在').aggregate(Count('id'))
#         # pass
#
#         '''
#         分组查询
#            -可以使用QuerySet对象.values('父表主键id').annotate(聚合函数('从表模型类名小写'))
#             -会自动连接两张表，然后使用外键字段作为分组条件
#             -如果从表外键设置了related_name，那么就不用使用从表模型类名小写，直接使用从表外键related_name即可
#         '''
#         qs = Projects.objects.values('id').annotate(Count('interfaces_projects'))
#         pass
#
#         '''
#         查询集QuerySet对象有什么特性？
#             -支持链式调用：可以在查询集上多次调用filter、exclude方法
#             -惰性查询：仅仅在使用数据时才会执行sql语句，为了提升数据库读写性能
#             -会执行sql语句的场景：len()、.count()、通过索引取值、print、for
#         '''
#
#     def post(self, request, pk):
#         '''
#         前端参数解析
#         1、前端传递参数的方式
#             -路径参数
#                 -在url路径中传递的参数，在请求实例方法中，使用关键字参数来接收
#             -查询字符串参数
#                 -url后面？后面的key value键值对参数，如http://www.xxxx.com/?key1=value1&key2=value2
#                 -request.GET获取
#                 -request.GET返回QueryDict,类似python中的dict类型
#                 -可以使用['key1']、get('key1')，会返回具体的值，如果有多个相同key的键值对，获取的是最后一个
#                 -getlist('key')，获取相同key的多个值，返回list类型
#
#
#         2、请求体参数
#             -json
#                 -json格式的参数会存放在body中，一般为字节类型byte
#                 -request.body去提取数据
#                 -json.loads(request.body)['gender'] 返回python中对数据类型，对数据进行转换(字典、嵌套字典类型)
#             -www-form-urlencoded
#                 -一般在网页前端中使用表单录入的参数
#                 -request.POST返回QueryDict,类似python中的dict类型
#             -file(multipart/data)
#                 -传递对文本数据 可以使用request.POST进行提取
#                 -传递对非文本数据(二进制文件),可以直接使用request.FILES去提取
#                 -如果传递纯粹对文件，request.body去提取
#             -请求头参数
#                 -第一种方式 直接使用request.headers['key']或者.get['key1']
#                 -第二种方式：request.META[HTTP_AUTHORIZATION']
#                     -请求头参数对可以被转化为参数名大写
#                     -去过参数命中含有—，会自动转化为_
#         '''
#         return HttpResponse("<h1>创建项目信息</h1>")
#
#     def put(self, request):
#         return HttpResponse("<h1>更新项目信息</h1>")
#
#     def delete(self, request):
#         return HttpResponse("<h1>删除项目信息</h1>")

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
        3、创建一条项目数据
        POST /projects/  新的项目数据以json的形式来传递
        '''
        # 获取所有项目数据（查询集），获取列表数据
        queryset = Projects.objects.all()

        # b.将项目的查询集数据转化为嵌套字典的列表
        project_list = []
        for item in queryset:
            item: Projects
            # project_dict = {
            #     'id':item.id,
            #     'name':item.name,
            #     'leader':item.leader
            # }
            project_list.append({
                'id': item.id,
                'name': item.name,
                'leader': item.leader
            })

        # 列表推导式
        # project_list = [{
        #         'id': item.id,
        #         'name': item.name,
        #         'leader': item.leader
        #     } for item in queryset]
        return JsonResponse(project_list, safe=False)

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
       4、更新一条项目数据
           PUT /projects/<int:pk>/   新的项目数据以json的形式来传递
       5、删除一条项目数据
           DELETE /projects/<int:pk>/
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
        python_data = {
            'id': project_obj.id,
            'name': project_obj.name,
            'msg': '获取数据成功'
        }
        return JsonResponse(python_data)

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

