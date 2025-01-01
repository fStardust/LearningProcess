"""
URL configuration for MyKit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounting/', include('accounting.urls')),

    # 登录和登出路径
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),     # 根路径映射至登录页
    # path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('logout/', LogoutView.as_view(next_page='logout'), name='logout'),     # Django 后台登出页面
]
