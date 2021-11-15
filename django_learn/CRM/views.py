from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
    return HttpResponse("hello,第一个django项目")


def detail(request,id,year,month):
    return HttpResponse("{}年{}月{}学号学生详情".format(year,month,id))


def student(request, name):
    return HttpResponse("{}学生".format(name))


def test1(request):
    return redirect('http://www.bing.com')


def login(request):
    # return redirect("/index/")  # 硬编码
    return redirect("index")    # url命名