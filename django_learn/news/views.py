from django.shortcuts import render
from django.views.generic import ListView, DetailView
from students.models import Student, StudentDetail
from django.db.models import Q
import math
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Create your views here.
@method_decorator(login_required, name='dispatch')
class StudentListView(ListView):
    section = "学生列表"
    template_name = 'students/student_list.html'  # 引用的是之前的students/student_list.html
    model = Student

    context_object_name = 'students'

    # paginate_by = 3  # 每页展示数据条数

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    # 优化：过滤+搜索

    # 查询功能
    def get_queryset(self):  # 过滤
        search = self.request.GET.get('search', '').strip()
        per_page = self.request.GET.get('per_page', 10)
        self.paginate_by = int(per_page)
        if search:
            if search.isdigit():
                sts = Student.objects.filter(Q(qq=search) | Q(phone=search), is_delete=False)
            else:
                sts = Student.objects.filter(name=search, is_delete=False)
        else:
            sts = Student.objects.filter(is_delete=False)

        students = sts.order_by('-c_time')  #
        self.students = students
        return students

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # 注意继承父类方法
        context['section'] = self.section
        context['per_page'] = self.paginate_by
        context['total_page'] = math.ceil(self.students.count() / int(context['per_page']))
        context['page'] = self.request.GET.get('page', 1)
        return context


class StudentDetailView(DetailView):
    section = "学生详情"
    template_name = 'students/student_detail.html'  # 引用的是之前的students/student_list.html
    model = Student  # 模型

    context_object_name = 'student'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # 注意继承父类方法
        context['section'] = self.section

        return context
