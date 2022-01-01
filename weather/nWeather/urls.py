from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),        # 主显示
    path('spider/', views.index, name='spider')     # 爬虫 并 存入数据库
]
