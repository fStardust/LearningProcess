from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'news'

urlpatterns = [
    path('student_list/', views.StudentListView.as_view(), name="student_list"),
    # path('student_list/', login_required(views.StudentListView.as_view()), name="student_list"),
    path('student_detail/<int:pk>', views.StudentDetailView.as_view(), name="student_detail"),


]
