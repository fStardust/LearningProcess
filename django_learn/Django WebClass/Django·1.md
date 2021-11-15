# Django·1

[TOC]

## 须知及前期知识

#### 须知

**代码主要展示核心代码，并非完整代码。（除标明外）**

#### 前期知识

python基础

简单Linux命令

MySQL



## web应用框架

### web应用框架介绍

1. web应用的本职还是**程序**
2. 程序分为服务器程序+应用程序
3. 服务器程序（Nginx、apache）类似发电厂，提供服务
4. 应用程序 类似用电器
5. WSGI--类似电源模块
6. web应用框架--类似电器模型/基本原理
7. web框架介绍

- Django 全能型web框架
- Web.py 小巧的web框架
- Tornado 异步的web框架

### 开发模式

<center>前后端部分分离的开发模式</center>

前端技术：html+css+js+jquery(ajax)

后端技术：Django + Django restframework +mysql + redis + celery + elaticsearch + nginx +uwsgi

（不一定都会用到）



| 技术点       | 说明                                                         |
| ------------ | ------------------------------------------------------------ |
| Mysql        | 双击热备、读写分离                                           |
| redis        | session缓存、图片验证码、短信验证码                          |
| elaticsearch | 站内搜索，Elaticsearch：实时分布式搜索分析引擎。（全文检索+结构化搜索+分析） |
| celery       | 异步发送短信                                                 |



### web部分设计模式

#### MTV

-m：models 模型--负责业务数据对象和数据库对象

-t：template 模板--负责把页面展示给用户（html）

-v：view视图--模型和模板的桥梁

#### MVC

-m：models 模型--负责业务数据对象和数据库对象

-v：view 视图--页面

-c：controller 控制器--接受用户的输入，调用模型和视图完成用户的请求。模型和视图的桥梁

## Django框架介绍及环境构建

#### 框架介绍

强调代码复用，轻便。

#### 环境搭建

Python3.5以上；Pycharm；MySQL（5.8） 建议 在Linux上搭建及使用 

```shell
# 步骤
# ** 以下主要在Linux中操作
1. 创建一个新的虚拟环境
	mkvirtualenv -p /usr/bin/python3 djangoApp
2. 通过pip安装djongo
	pip install django==2.1.7
3. cd 项目文件将要存放的位置
	cd project
4. 选择和编辑器版本无关的通用方式创建项目-->即命令行："django-admin startproject 项目名"
	django-admin startproject CRM
5. 至此django服务器已经配置完成

验证环境
6. 进入刚刚创建的项目，查看目录
	ls
	-->CRM manage.py
7. 运行manage.py "python manage.py runserver IP:端口号"**注意CONTROL-C 退出服务
	python manage.py runserver 0.0.0.0:8000
8. 通过浏览器访问服务器 主机号:端口号"127.0.0.1:8000"
	出现 火箭及安装成功提示，如下。
"The install worked successfully! Congratulations!"
	

## 0.0.0.0 所有外网IP都可访问该服务
## 8000是django的默认远程访问端口


# 补充：
## PyCharm连接Python虚拟解释器时不要使用系统路径下的解释器。
## 查看当前有哪些虚拟环境
workon
## 切换/进入当前虚拟环境："workon 环境名"
workon djangoApp
## 创建虚拟环境："mkvirtualenv -p 复制地址 虚拟环境命名"
mkvirtualenv -p /usr/bin/python3 djangoApp
## 退出虚拟环境
deactivate
## 删除虚拟环境 "rmvirtualenv 环境名"
rmvirtualenv djangoApp

```

![django初始界面](https://i.loli.net/2021/03/15/QLGbn7JD4PMk3jO.png)

#### 配置PyCharm远程同步

```
用PyCharm在本地创建一个新项目
配置远程解释器（注意：与项目解释器一致）
注意：同一个解释器不要配置多个路径
修改文件映射路径
设置自动同步

配置完成后即能在PyCharm界面右侧，点击RemoteHost，看见保存目录
```

#### PyCharm中运行项目

```
1.命令行方法		2.设置中配置

在PyCharm中选择Tools中的Stack SSH Session...
在弹出窗口中选择刚刚创建的远程环境
控制台即可连接虚拟机
在控制台中可通过相应的命令运行django

进入 Configurations窗口
添加Django Server服务
在右侧修改：重命名、主机号、端口号
并保存
在Settings找到Django并点击
在右侧勾选Enable Django Support
并选择主机文件位置 与 Settings文件位置
并保存

此时PyCharm上方的运行文件框中有CRM
运行即可完成
```

### 文件介绍与路由命令

#### 项目文件介绍

![CRM文件目录](https://i.loli.net/2021/03/17/Xrh42cZPEWCUkMg.png)

CRM
    ├── CRM
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-35.pyc
    │   │   ├── settings.cpython-35.pyc  --配置文件
    │   │   ├── urls.cpython-35.pyc --路由文件
    │   │   └── wsgi.cpython-35.pyc --接口文件
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── db.sqlite3 --自带的小数据库
    └── manage.py --启动项目及命令实现

#### 第一个视图

在CRM中创建views.py 并输入 代码 --所要显示在界面上的内容

在urls.py 中 导入该文件 及方法 

运行后，可在浏览器内输入 127.0.0.1:8000/index/ 可见内容

代码及详细内容如下：

![详细内容](https://i.loli.net/2021/03/17/puqlGYjwhesncz4.png)



#### url路由及模板渲染方式

##### 创建应用：

在命令行中输入：“python manage.py startapp teacher”

即创建teacher的应用文件

##### 路由系统(urls.py)

**URL：全球统一资源定位符**

url=协议 + 域名（ip地址和端口）[ + 路径 +参数]

urls.py --路由文件/路由系统/URL配置-->实现url路径到视图函数的一个映射

1.  文件内urlpatterns代码参数：

    1.  `path(route, view,kwargs=None,name=None)`
    2.  Route：字符串，url的路径
    3.  View：视图
    4.  Kwargs：额外参数，格式字典，直接传递给视图。<!--当kwargs中key与url捕获的key一致时，以kwargs为准。-->
    5.  Name：命名，用于跳转指定

2.  path--`path(route, view,kwargs=None,name=None)`

    1.  路径转换器：`<转换器:参数名>` 

    2.  转换器有：str(默认)、int、Uuid

    3.  转换器可叠加，中间可用符号做间隔

    4.  ```
        urls.py中代码：
        path('detail/<int:id>-<int:year><int:month>/', views.detail)
        
        浏览器输入：
        http://127.0.0.1:8000/detail/18-201912/
        浏览器输出：
        20191年2月18学号学生详情
        ```

    5.  无法控制控制器内传入数据的格式

3.  re_path--`re_path(route, view,kwargs=None,name=None)`

    1.  命名正则表达式分组的语法`(?P<>正则表达式)`

    2.  可以使用正则表达式来限制参数

    3.  ```
        re_path(r'detail/(?P<id>\d+)/(?P<year>\d{4})(?P<month>[0-9]|1[0-2])/', views.detail)
        
        浏览器输入：http://127.0.0.1:8000/detail/18/201912/
        浏览器输出：
        2019年12月18学号学生详情
        ```

4.  Kwargs

    1.  ```
        urls.py:
        path("student/", views.student, kwargs={'name': '张三'})
        
        views.py:
        def student(request,name):
            return HttpResponse("{}学生".format(name))
        ```

5.  重定向

    1.  `from django.shortcuts import redirect`

    2. ```
        代码：
        def test1(request):
            return redirect('http://www.bing.com')
            
        -->跳转至：必应
        ```

    3. 硬编码
       
        ```
        代码：
        def login(request):
            return redirect("/index/")
            
        -->跳转至：index
        
        此时 url.py中 path--index内容为
        path('index/', views.index)
        若route处修改，跳转失效
        ```
        
    4.  url命名

        ```
        代码：
        return redirect("index")    # url命名
        
        -->跳转至：index/ZhangSan
        
        此时 url.py中 path--index内容为
        path('index/ZhangSan',views.index,name='index')
        ```

6.  包含其他URLconf：include

    1.  实际开发中吗，我们的视图都在app中
    2.  使连接结构更加清晰，易于维护
    3.  在CRM中的url.py中添加`path("teacher/", include('teacher.urls'))`可以跳转并使用teacher文件夹中的urls。
    4.  **谨慎使用** 在CRM中的ｕｒｌｓ．ｐｙ文件中使用参数（包括kwarges），会传递到ｉｎｃｌｕｄｅ下面包含的每一个路径．代码如下：
        - `path("teacher/<name>",include('teacher.urls')),`。     

7.  App_name

    1.  index与login在不同的app中都会用到，所以需要做好区别

    2.  未使用App_name

        ```python
        # CRM/urls.py
        from django.contrib import admin
        from django.urls import path, re_path, include
        from . import views
        urlpatterns = [
            path('index/ZhangSan', views.index,name='index'),
            path("students/", include('students.urls')),
        ]
        
        # CRM/views.py
        from django.http import HttpResponse
        from django.shortcuts import redirect
        def index(request):
            return HttpResponse("hello,第一个django项目")
        def login(request):
            return redirect("index")
        
        # students/urls.py
        from django.urls import path, re_path, include
        from . import views
        urlpatterns = [
            path("index/", views.index, name="index"),
            path("login/", views.login, name="login"),
        ]
        
        # students/view.py
        from django.http import HttpResponse
        from django.shortcuts import render, redirect
        def index(request):
            return HttpResponse("主页")
        
        def login(request):
            return redirect("index") 
        
        
        """
        此时在浏览器中输入：
        	127.0.0.1:8000/students/index/
        显示的是：
        	hello,第一个django项目
        
        原理：
        	CRM/urls.py"7"-->students/urls.py"22"-->CRM/urls.py"6"-->CRM/views.py"13，14"-->执行CRM/views.py"14"
        
        注：原理中""内的是本代码块中的行号
        """
        ```

    3.  使用App_name

        ```python
        # CRM/urls.py
        from django.contrib import admin
        from django.urls import path, re_path, include
        from . import views
        urlpatterns = [
            path('index/ZhangSan', views.index,name='index'),
            path("students/", include('students.urls')),
        ]
        
        # CRM/views.py
        from django.http import HttpResponse
        from django.shortcuts import redirect
        def index(request):
            return HttpResponse("hello,第一个django项目")
        def login(request):
            return redirect("index")
        
        # students/urls.py
        from django.urls import path, re_path, include
        from . import views
        app_name = 'student'
        urlpatterns = [
            path("index/", views.index, name="index"),
            path("login/", views.login, name="login"),
        ]
        
        # students/view.py
        from django.http import HttpResponse
        from django.shortcuts import render, redirect
        def index(request):
            return HttpResponse("主页")
        def login(request):
            return redirect("student:index")    # app_name:name **注意此项中的app_name只跟students/urls.py中的app_name = 'student'相关
        
        
        """
        此时在浏览器中输入：
        	127.0.0.1:8000/students/index/
        显示的是：
        	主页
        
        原理：
        	CRM/urls.py"7"-->students/urls.py"23"-->CRM/urls.py"6"-->students/view.py"30，31"-->执行CRM/views.py"31"
        
        注：原理中""内的是本代码块中的行号
        """
        ```

8.  总结：

    1.  当一个请求过来使，django先从根url配置中进行路由规则匹配（本笔记中CRM为根url配置）
    2.  如果这个路由规则找到的path中有include，则去找这个include包含的url配置
    3.  访问的url由路由规则决定


## 补充知识

### 概念

1. 软连接：类似快捷方式
2. 虚拟环境：
   1. 虚拟环境就是复制了一个新的解释器
   2. 不同项目同一个解释器会导致项目崩溃
3. 先找到进程号，再杀死`Ps -ef|grep 8000` -->`kill 进程号`
4. 应用端程序和服务器端程序通常是多对一的关系
   1. 即一个服务器端程序，面向众多客户端提供数据服务。
   2. 网站：只需写服务端，浏览器即为客户端程序-->这是B/S结构的优势
5. 数据库与服务器端的关系
   1. 数据库只是服务器端的一部分
   2. 数据库是存储的数据并没有业务逻辑
   3. 逻辑需要依靠程序实现
