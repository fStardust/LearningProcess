from datetime import datetime
import os
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View

# Create your views here.
from django.template.loader import get_template
from teacher.models import Student
from CRM.settings import MEDIA_ROOT
from teacher.forms import RegisterForm


def students(request):
    return HttpResponse("成功")


def login(request):
    return redirect("teacher:index")


def test1(request):
    name = "小光"
    # return HttpResponse('<h1>我是前端代码<h1>')
    # t = get_template('teacher/test.html')   # 获取到页面
    # html = t.render()     # 文件渲染
    # return HttpResponse(html)
    return render(request, 'teacher/test.html', context={'name': name})


def index(request):
    num = request.COOKIES.get('num')
    if num:
        num = int(num) + 1
    else:
        num = 1

    now = datetime.now()
    # now = datatime.now.strftime('%Y年%m月%d日 %H：%M：%S')  # datetime下的时间格式
    date_format = "Y年m月d日 H: i:s"  # django下的时间格式
    format_str = '%Y年%m月%d日 %H：%M：%S'
    lt = [4, 5, 6]
    dt = {"name": "张三", "age": 18, "height": 183}
    # sts = [
    #     {"name": "张三", "age": 18, "height": 183, 'sex': 1, 'course': ['python', 'java', 'C++', 'web前端']},
    #     {"name": "李四", "age": 18, "height": 183, 'sex': 1, 'course': ['python', 'java', 'C++', 'web前端']},
    #     {"name": "王五", "age": 18, "height": 183, 'sex': 0, 'course': ['python', 'java', 'C++', 'web前端']},
    # ]
    sts = Student.objects.all()
    response = render(request, "teacher/index.html", context={
        "num": num,
        'now': now,
        'date_format': date_format,
        "lt": lt,
        "dt": dt,
        "students": sts,
        'format_str': format_str,
    })
    response.set_cookie('num', num, max_age=5)  # max_age设置cookie的有效值，5秒后重置
    return response

    # return render(request, "teacher/index.html", context={
    #     "num": num,
    #     'now': now,
    #     'date_format': date_format,
    #     "lt": lt,
    #     "dt": dt,
    #     "students": sts,
    #     'format_str': format_str,
    # })


def login(request):
    if request.method == 'POST':
        # file = request.FILES.get('file')    # 上传一个文件
        files = request.FILES.getlist('file')  # 上传多个文件
        # 每天的文件放到每天的文件夹中
        day_dir = datetime.now().strftime('%Y%m%d')
        dir_path = os.path.join(MEDIA_ROOT, day_dir)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        for file in files:
            filename = os.path.join(dir_path, file.name)
            with open(filename, 'wb')as f:
                for line in file.chunks():  # chunks--上传文件过大时，自动分块
                    f.write(line)

    # 请求
    # # if request.method == 'GET':
    # #     return render(request, "teacher/login.html")
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     if username == 'qwe' and password == 'qwe':
    #         return redirect('teacher:index')
    #     # else:
    #     #     return render(request, "teacher/login.html")
    return render(request, "teacher/login.html")


def detail(request, name):
    return HttpResponse("{}详情，恭喜成功".format(name))


def test_json(request):
    sex = request.GET.get('sex')
    sex = int(sex)
    res = Student.objects.values('name', 'age', 'sex').filter(sex=sex)
    res = list(res)
    data = {'result': res}
    return JsonResponse("ok")


def register(request):
    if request.method == 'GET':
        form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)  # 实例化对象，此时的对象有了你填入的数据

        if form.is_valid():  # 字段校验，成功返回True
            password = form.cleaned_data.get('password')
            password_repeat = form.cleaned_data.get('password_repeat')
            if password == password_repeat:
                return HttpResponse('注册成功')

    return render(request, 'teacher/register.html', context={
        'form': form,
    })


class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'teacher/register.html', context={
            'form': form,
        })

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():  # 字段校验，成功返回True
            password = form.cleaned_data.get('password')
            password_repeat = form.cleaned_data.get('password_repeat')
            if password == password_repeat:
                return HttpResponse('注册成功')

        return render(request, 'teacher/register.html', context={
            'form': form,
        })


def my_view(request):
    if request.method == 'GET':
        return HttpResponse('ok')


class MyView(View):
    def get(self, request):
        return HttpResponse("oh")
