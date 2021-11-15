from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse
from .models import Student, Grade, StudentDetail
from .forms import StudentForm, StudentDetailForm


# Create your views here.
@permission_required('students.view_student', raise_exception=True)
@login_required
def student_list(request):
    # # 确认是否有权限
    # if request.user.has_perm('students.view_student'):
    #     return HttpResponse('你无权查看')

    # # 限制登录
    # if not request.user.is_authenticated:  # 未登录用户访问，返回登录页面
    #     return redirect(reverse('student:login') + '?next={}'.format(request.path_info))
    #     # student/login/?next="student/student_list/"

    section = "学生列表"

    # 查询功能
    search = request.GET.get('search', '').strip()

    if search:
        if search.isdigit():
            sts = Student.objects.filter(Q(qq=search) | Q(phone=search), is_delete=False)
        else:
            sts = Student.objects.filter(name=search, is_delete=False)
    else:
        sts = Student.objects.filter(is_delete=False)

    sts = sts.order_by('-c_time')  # 排序

    # 实现分页：
    # 数据总量
    total_num = sts.count()
    # 每页数据条数
    per_page = request.GET.get('per_page', 10)
    # 当前页码
    page = request.GET.get('page', 1)

    paginator = Paginator(sts, per_page)
    sts = paginator.get_page(page)
    total_page = paginator.num_pages

    return render(request, 'students/student_list.html', context={
        "section": section,
        "search": search,
        "students": sts,
        "per_page": per_page,
        "total_page": total_page,
        "page": page,
    })


def student_detail(request, pk):
    section = "学生详情"
    student = Student.objects.get(pk=pk)
    return render(request, 'students/student_detail.html', context={
        "section": section,
        "student": student,
    })


def student_add(request):
    section = "添加学生"
    if request.method == 'GET':
        return render(request, 'students/student_detail.html', context={
            "section": section,
        })

    if request.method == 'POST':
        # 接收数据 并保存到数据库
        # 1.获取学生信息
        data = {
            'name': request.POST.get('name'),
            'age': request.POST.get('age'),
            'sex': request.POST.get('sex'),
            'qq': request.POST.get('qq'),
            'phone': request.POST.get('phone'),
            'grade_id': request.POST.get('grade'),
        }
        student = Student.objects.create(**data)
        # 2.获取学生详情并保存
        StudentDetail.objects.create(
            college=request.POST.get('college'),
            student=student  # 表关联
        )
        return redirect("student:student_list")


def student_delete(request, pk):
    student = Student.objects.get(pk=pk)
    student.is_delete = True
    student.save()
    return redirect("student:student_list")


def student_edit(request, pk):
    section = "学生信息修改"
    student = Student.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'students/student_detail.html', context={
            "section": section,
            "student": student,
        })
    if request.method == 'POST':
        # 学生列表
        grade_id = request.POST.get('grade')
        try:
            grade = Grade.objects.get(pk=grade_id)
        except:
            grade = None

        student = Student.objects.get(pk=pk)
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.sex = request.POST.get('sex')
        student.qq = request.POST.get('qq')
        student.phone = request.POST.get('phone')
        student.grade = grade  # 表关联

        # 学生详情
        try:
            student_detail = student.studentdetail  # 反向查找
        except:
            student_detail = StudentDetail()  # 正向
            student_detail.student = student

        student_detail.college = request.POST.get('college')

        student_detail.save()
        student.save()

        return redirect('student:student_list')


def index(request):
    name = request.session.get('name', "游客")

    return render(request, 'students/index.html', context={
        "name": name,
    })


def detail_form(request, pk):
    section = "学生信息修改"
    student = Student.objects.get(pk=pk)
    form = StudentForm(instance=student)
    try:
        detail_form = StudentDetailForm(instance=student.studentdetail)
    except:  # 如果学生没有详情
        student_detail = StudentDetail()
        student_detail.student = student
        student_detail.save()
        detail_form = StudentDetailForm(instance=student_detail)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        detail_form = StudentDetailForm(request.POST, instance=student.studentdetail)

        if form.is_valid() and detail_form.is_valid():
            form.save()
            detail_form.save()

            return render(request, 'students/student_list.html')

    return render(request, 'students/detail_form.html', context={
        'section': section,
        'form': form,
        'detail_form': detail_form,
    })


# def login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST.get('password')
#         if username == 'qwe' and password == 'qwe':
#             request.session['name'] = username
#             request.session.set_expiry(10)  # 设置过期时间，10秒重置
#
#             return redirect("student:index")
#
#     return render(request, "students/login.html")


# def logout(request):
#     request.session.flush()
#     return redirect('student:index')


def login_view(request):
    # user = request.user
    # 限制登录优化一
    next_url = request.GET.get('next')
    # 判断是否登录
    if request.user.is_authenticated:  # 匿名用户返回false
        if next_url:
            return redirect("next_url")

    if request.method == 'POST':
        # 获取用户名密码
        username = request.POST.get('username')
        password = request.POST['password']
        # 校验用户名和密码
        user = authenticate(username=username, password=password)  # 正确返回user对象，错误返回的None
        if user is not None:
            # 用户信息存放到session并登录
            login(request, user)

            # 限制优化一
            if next_url:
                return redirect(next_url)
            return redirect("student:index")
    return render(request, "students/login.html")


def logout_view(request):
    logout(request)
    return redirect('student:index')
