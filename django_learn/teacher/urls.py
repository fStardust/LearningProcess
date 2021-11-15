"""teacher URL Configuration

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

app_name = 'teacher'

urlpatterns = [
    path("students/", views.students),
    path("detail/<name>", views.detail, name="detail"),
    path("login/", views.login, name="login"),
    path("test1/", views.test1, name="test1"),
    path("index/", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("test_json/", views.test_json, name="test_json"),
    path("my_ok/", views.my_view, name="my_ok"),
    path("my_oh/", views.MyView.as_view(), name="my_oh"),
    path("register/", views.register, name="register"),
    path("register_new/", views.Register.as_view(), name="register_new"),
]
