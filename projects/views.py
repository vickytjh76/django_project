from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.

# def index(request):
#     return HttpResponse('Http')
#
# def get_projects(request, pk):
#     return HttpResponse("get_projects")
#
# def get_project1(request):
#     return HttpResponse("get_project1")
#
#
# def create_project(request):
#     return HttpResponse("create_project")
#
# def put_project(request):
#     return HttpResponse("put_project")
#
# def delete_project(request):
#     return HttpResponse("delete_project")

def projects(request):
    """
    视图函数
    a.视图函数的第一参数是HttpRequest对象
    b.HttpRequest对象包含了请求的所有数据（请求头、请求体）
    c.视图函数必须得返回一个HttpResponse对象或者其子类对象
    :param request:
    :return:
    """
    # print(request)
    # print(type(request))
    # print(type(request).__mro__)
    # if request.method == 'GET':
    #     return HttpResponse("<h1>获取项目信息</h1>")
    # elif request.method == 'POST':
    #     return HttpResponse("<h1>创建项目信息</h1>")
    # elif request.method == 'PUT':
    #     return HttpResponse("<h1>更新项目信息</h1>")
    # elif request.method == 'DELETE':
    #     return HttpResponse("<h1>删除项目信息</h1>")
    # else:
    #     return HttpResponse("<h1>其他操作</h1>")

# 在views.py中定义的函数，称为视图函数
from django.views import View
import json

class ProjectView(View):
    """
    一、定义类视图
    1.继承View或者View子类
    2.不同的请求方法有相应的方法进行对应
        GET   ->   get
        POST  ->   post
        PUT   ->   put
        DELETE ->  delete
        PATCH  -> patch
    3.每一个处理请求的方法，必须得返回HttpResponse对象或者HttpResponse子类对象
    4.每一个处理请求的方法，第二个参数request必须为HttpRequest对象
    """

    def get(self, request, pk):
        project_data = {
            'id': 1,
            'name': 'XXX项目',
            'leader': '潘潘达'
        }

        project_data_list = [
            {
                'id': 1,
                'name': 'xxxx项目',
                'leader': '潘潘达'
            },
            {
                'id': 2,
                'name': 'yyyy项目',
                'leader': '多喝热水'
            },
            {
                'id': 3,
                'name': 'zzzz项目',
                'leader': '不语'
            }
        ]

        # json_str = json.dumps(project_data, ensure_ascii=False)
        # return HttpResponse(json_str, content_type='application/json')  #将json的字符串，返回给前端

        return JsonResponse(project_data_list, json_dumps_params={'ensure_ascii':False}, safe=False)

    def post(self, request):
        return HttpResponse("<h1>创建项目信息</h1>")

    def put(self, request):
        return HttpResponse("<h1>更新项目信息</h1>")

    def delete(self, request):
        return HttpResponse("<h1>删除项目信息</h1>")