"""CRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/ZhangSan', views.index, name='index'),
    re_path(r'detail/(?P<id>\d+)/(?P<year>\d{4})/(?P<month>[0-9]|1[0-2])/', views.detail),
    path("student/", views.student, kwargs={'name': '张三'}),
    path("test1/", views.test1),
    path("login/", views.login),
    # path("teacher/<name>", include('teacher.urls')),    # 注意此参数会传递到include的下面包含的每一个路径
    path("teacher/", include('teacher.urls')),
    path("students/", include('students.urls')),
    path("news/", include("news.urls")),
    path("", include("polls.urls"))
]
