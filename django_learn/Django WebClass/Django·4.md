# Django·4

[toc]

## 请求与相应

### HttpRequest对象

django框架是一个web应用框架

请求和响应的流程：

```
输入网址，请求页面，通过路径找到对应视图函数。
django船舰的HTTPRequest对象，该对象包含了关于请求的源数据
经过处理，视图返回一个HttpResponse对象
```



```


from django.core.paginator import Paginator

p = Paginator(Student.objects.all().order_by('-c_time'), 3) 
```

GET：请求

POST：提交



## 完善功能

<center>使用开源组件和Django进行功能完善和界面优化</center>

#### 主要功能

完成基本数据库搭建后,要面向使用者进行功能完善。

基本功能：

查询；添加；编辑；删除；详情；退出；注册/登录; 重置；分页……

学习阶段可先用开源组件（前端方法）先将大致界面功能实现，再用django替换/完善/优化相关功能及代码。

##### 动态页面--cookie

cookie直接返回访问者信息，不做隐藏，不够安全。

session基于cookie，对敏感信息做了隐藏，相对安全--session_id关联敏感信息，不直接展示。

* 且django中已经注测了sessionAPP



## Django快捷模块

#### Django表单

<center>通过django模块实现登录退出</center>

1. 简单表单--forms.Form

   1. 本质上是是一个类

   2. form表单标签 以及提交按钮需要手动加入

   3. 自定义校验：

      - ```python
         实现确认密码时,密码不一致的提示--采用多字段验证
         # 多字段
         def clean(self):    
         	pass
         
         # 单字段
         def clean_password(self):
         	pass
         	
         # \CRM\teacher\forms.py
         
         class RegisterForm(forms.Form):
             username = forms.CharField(label='用户名', max_length=20)
             password = forms.CharField(
                 label='密码', max_length=8, min_length=6,
                 widget=forms.PasswordInput(attrs={'placeholder': '请输入6-8位长度密码'}),
                 error_messages={'min_length': '密码长度小于6位', 'max_length': '密码长度大于6位', }
             )
             password_repeat = forms.CharField(label='确认密码', widget=forms.PasswordInput())
             def clean(self):    # 多字段
                 cleaned_data = super().clean()      # 继承父类
         
                 # 增加提示信息
                 password = cleaned_data.get('password')
                 password_repeat = cleaned_data.get('password_repeat')
         
                 if password != password_repeat:
                     msg = '密码不一致'
                     self.add_error('password_repeat', msg)
         ```

2. 模型表单--forms.ModelForm

       1. ```python
                from django import forms
                from students.models import Student, StudentDetail
   
   
   ​             
   ​             class StudentForm(forms.ModelForm):
   ​                 class Meta:
   ​                     model = Student  # 模型
   ​                     fields = '__all__'
   ​                     
   ​             class StudentDetailForm(forms.ModelForm):
   ​                 class Meta:
   ​                     model = StudentDetail  # 模型
   ​                     fields = '__all__'
   ​                     
   ​          # Fields = "__all__" and __all__ = [' bar ', 'baz'] usage is the same,It's just that the former is at the front end of the code, and the latter can be added to any class at will, making it easier to write.
   ​       ```
   
      2. ```html
            # 前端样式展示
            ## 在之前的前端框架中嵌入forms.py中的内容
            {% for field in form %}
                    <div class="form-group">
                        <label for="{{ field.id_for_label }}" class="col-sm-2 control-label">{{ field.label }}</label>
                        <div class="col-sm-2">
                            {% add_class field "form-control" %}
                        </div>
                        {#      错误展示        #}
                        {% for error in field.errors %}
                            <label for="{{ field.id_for_label }}" class="col-sm-2 control-label {% if field.errors %} has-error {% endif %}">{{ error }}</label>
                        {% endfor %}
                    </div>
                {% endfor %}
         ```
   
   
   
   #### 中间件
   
   中间件文件可以放在项目路径下的任何位置，类似视图函数，接受request，返回response
   
      ```python
      # teacher/Middleware.py
      
      ## 激活中间件：路径添加至:CRM\settings.py--MIDDLEWARE
      
      ### 中间件可以是函数，也可以是类
      
      from django.http import HttpResponseForbidden
      
      
      def simple_middleware(get_response):  # 参数名不可更改
          print('初始化设置1')
      
          def middleware(request):
              # 只有谷歌浏览器才让访问
              user_agent = request.META['HTTP_USER_AGENT']
              if not 'chrome' in user_agent.lower():
                  return HttpResponseForbidden()
      
              print("处理请求前执行的代码1")
              response = get_response(request)
              print("处理请求后执行的代码2")
              return response
      
          return middleware
      
      
      class SimpleMiddleWare:
          def __init__(self, get_response):
              self.get_response = get_response
              print('初始化设置2')
      
          def __call__(self, request):
              print("处理请求前执行的代码3")
              response = self.get_response(request)
              print("处理请求后执行的代码4")
              return response
      
      
      ```



#### 上下文处理器

`context_processors`

context传递变量到模板，如果所有页面都需要某些传递变量，就可以使用上下文处理器。

```python
# 案例：加入所有页面都需要一个name变量

# teacher/customer_context_processor.py
## 需要配置：在\CRM\settings.py--TEMPLATES-'OPTIONS'-'context_processors'中添加路径

相同的key，context生效。

```

## django_admin

django提供的完善基本管理系统

通过`python manage.py createsuperuser` 创建用户进行登陆

![admin](https://i.loli.net/2021/04/17/vE6DYNt5MmX3rsk.png)

在setting.py中的`LANGUAGE_CODE`可以修改语言

![admin1](https://i.loli.net/2021/04/17/klsGSJC2thRFZTL.png)

数据：来自app下的admin.py中注册要管理的模块。

![django-1](https://i.loli.net/2021/04/17/bVpJscK3OSNqI5t.png)



#### 验证登录及限制直接访问

 [官方文档](https://docs.djangoproject.com/zh-hans/3.2/topics/auth/) 

使用django自带的用户身份验证系统：

1. 用户验证：登录的账号是否是真的用户
2. 授权：不同类型账户给不同权限

功能要求：验证登录-->退出-->限制直接访问数据页面

1. 验证登录

   ```python
   # views.py
   def login_view(request):
       # user = request.user
       # 判断是否登录
       if request.user.is_authenticated:  # 匿名用户返回false
           return redirect("student:student_list")
   
       if request.method == 'POST':
           # 获取用户名密码
           username = request.POST.get('username')
           password = request.POST['password']
           # 校验用户名和密码
           user = authenticate(username=username, password=password)  # 正确返回user对象，错误返回的None
           if user is not None:
               # 用户信息存放到session并登录
               login(request, user)
           return redirect("student:student_list")
       return render(request, "students/login.html")
   
   
   ```

   ```html
   {# index.html #}
   <body>
       欢迎{{ user.username|default:'游客' }}访问
   
       {% if user.is_authenticated %}
       <a href="{% url "student:logout" %}">退出</a>
       {% else %}
       <a href="{% url "student:login" %}">登录</a>
       {% endif %}
   </body>
   ```

   

2. 退出

   ```python
   def logout_view(request):
       logout(request)
       return redirect('student:index')
   ```

3. 实现限制

   ```python
   # views.py
   def student_list(request):
       # 限制登录
       if not request.user.is_authenticated:  # 未登录用户访问，返回登录页面
           return redirect('student:login')
   	...
   ```

4. 限制优化

   ```python
   # 登录优化一
   ## 实际开发过程中，如果要访问某个页面，而这个页面需要登录权限，登录后自动跳转会此前我想访问的页面
   #-> 将当前的路径当作参数传入

   def student_list(request):
       # 限制登录
       if not request.user.is_authenticated:  # 未登录用户访问，返回登录页面
           return redirect(reverse('student:login') + '?next={}'.format(request.path_info))
   
   # 登录优化二
   ## 多视图函数，同时需要添加这个功能，会造成代码冗余
   #-> 装饰器
   @login_required 
   解析->↓&&替换优化一中函数内容
   http://127.0.0.1:8000/accounts/login/?next=/students/student_list/
   
   #* 其中唯一不同之处--accounts 需要在settings.py中修改以替换为所需内容
   ## 添加内容：
   LOGIN_URL = reverse_lazy('student:login')
   
   ```
   

#### 授权系统

##### 增添权限

可视化：在[django_admin](http://127.0.0.1:8000/admin/) 中添加管理用户，与权限分组

在命令行中给组增添权限：

```python shell
In [1]: from django.contrib.auth.models import User, Group, Permission 
In [2]: User.objects.all()
Out[2]: <QuerySet [<User: qwe>, <User: py_vip>, <User: myU>]>
    
In [3]: u1 = User.objects.last()
In [4]: g1, g2 = Group.objects.all() 
In [5]: u1.groups
Out[5]: <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager at 0xb476aacc>
    
In [6]: u1.groups.add(g1) # 给u1组g1权限
In [7]: u1.groups.clear()	# 删除
In [9]: u1.groups.set([g1,g2])# 功能如上
In [10]: u1.groups.remove(g1,g2)
In [11]: u1.user_permissions  
Out[11]: <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager at 0xb1df6a4c>
    
In [12]: u1.user_permissions.set([1,5,7,9])# 逐条加权限
In [13]: u1.user_permissions.add(2,4)
In [14]: u1.user_permissions.remove(2,4)
In [15]: u1.user_permissions.clear()
    
# 总结：跟之前的增删改查操作差别不大，注意控制器的不同
```

![权限](https://i.loli.net/2021/04/18/uvfAV95az1IiDUm.png)

##### 授权限制

权限验证

```python
def student_list(request):
    # 确认是否有权限
    if request.user.has_perm('students.view_student'):
        return HttpResponse('你无权查看')
    ...
        
# 可以替换为-->
from django.contrib.auth.decsorators import permission_required

@permission_required('students.view_student', raise_exception=True)
def student_list(request):
    ...
```

应用至前端--模板中使用

```html
{# 如果有添加权限-->再显示添加按钮#}
{% if perms.students.add_student %}
<a href="{% url 'student:add' %}" class="btn btn-primary">添加</a>
{% endif %}
```

应用实例 :point_down:

![权限web](https://i.loli.net/2021/04/18/qIutUKwSbnmjYkc.png)

## 类试图

##### 类视图基本用法

```python
# 类视图
class MyView(View):
    def get(self, request):
        return HttpResponse("oh")
    
# 路径配置    
path("my_oh/", views.MyView.as_view(), name="my_oh"),
```

```python
# 之前长期使用的 函数视图
def my_view(request):
    if request.method == 'GET':
        return HttpResponse('ok')

# 路径配置
path("my_ok/", views.my_view, name="my_ok"),
```

#### 类视图使用表单

1. 原先函数视图表单

   ```python
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
   
   # 路径：path("register/", views.register, name="register"),
   ```

2. ```
   
   # 路径 path("register_new/", views.Register.as_view(), name="register_new"),
   ```

   

#### 通用视图

1. ListView

   1. ```
      学生列表修改为ListView
      -->\CRM\news\views.py 中
      ```

      

2. DetailView

   1. ```
      学生详情修改为DetailView
      -->\CRM\news\views.py 中
      ```

      





#### 类试图装饰器

1. URLconf中

   1. ```python
      from django.contrib.auth.decorators import login_required
      
      app_name = 'news'
      
      urlpatterns = [
          # path('student_list/', views.StudentListView.as_view(), name="student_list"),
          path('student_list/', login_required(views.StudentListView.as_view()), name="student_list"),
          path('student_detail/<int:pk>', views.StudentDetailView.as_view(), name="student_detail"),
      
      
      ]
      ```

2. 装饰类

   1. ```python
      from django.utils.decorators import method_decorator
      from django.contrib.auth.decorators import login_required
      
      class StudentListView(ListView):
      @method_decorator(login_required)
      	def dispatch(self, request, *args, **kwargs):
          	return super().dispatch(*args, **kwargs)
          ...
      ```

   2. ```python
      @method_decorator(login_required, name='dispatch')
      class StudentListView(ListView):
      ```
