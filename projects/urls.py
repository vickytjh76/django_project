# !/usr/bin/env python3
# coding=utf-8

"""
@Desc: 
@Author: Vicky
@Time: 2021/04/29
"""


from django.urls import path
from projects import views

urlpatterns = [
    path('get/', views.get_projects),
    path('create/', views.create_project),
    path('put/', views.put_project),
    path('delete/', views.delete_project),
    path('a/', views.delete_project)
]