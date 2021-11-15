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

app_name = 'student'

urlpatterns = [
    path('student_list/', views.student_list, name='student_list'),
    path('student_detail/<pk>/', views.student_detail, name='detail'),
    path('student_delet/<pk>/', views.student_delete, name='delete'),
    path('student_edit/<pk>/', views.student_edit, name='edit'),
    path('student_add/', views.student_add, name='add'),
    # path('login/', views.login, name='login'),
    path('login/', views.login_view, name='login'),
    # path('logout/', views.logout, name='logout'),
    path('logout/', views.logout_view, name='logout'),
    path('index/', views.index, name='index'),
    path('detail_form/<pk>/', views.detail_form, name='detail_form'),
]
