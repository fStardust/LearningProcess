# Django·2

[toc]

## 须知

**代码主要展示核心代码，并非完整代码。（除标明外）**

## 模板变量及过滤器

### 模板系统

将html文件作为模板写到模板文件中。

1. 集中放到一个目录（templates）中

   1. 模板要放到特定的文件夹中，在项目根目录（和manage同级）下创建一个文件夹。
   2. 在CRM/setting.py中的TEMPLATES=[{'DIRS[]'}]中添加路径如下：`'DIRS': [os.path.join(BASE_DIR,'templates')],`
   3. 在templates文件夹下对应app创建对应文件夹存储模板文件（本质是html）

   

2. 模板app目录下templates文件夹下

   1. 在app下创建templates文件夹
   2. 配置：在setting中的INSTALLED_APPS添加app名即可

3. 总结

   1. 模板的两种存放方式
   2. 如何选择：
      1. 一般情况下，选择集中存放
      2. 如果app需要重复使用，选择在app下建模板
      3. 区分不同应用的同名模板：templates文件夹下创建app文字命名

### 模板

**动态页面**

1. 模板变量的语法：{{变量名}}
   
   1. 变量命名规则
   2. {{模板变量名|过滤器}}
   3. {{模板变量名|过滤器:字符串变量/模板变量}}
   4. “:”前后不能空格
   5. 可以链式操作
   6. 
   
2. 模板过滤器

   1. 可以在模板文件上直接对模板变量进行处理

   2. 常用过滤器

      ```
      add
      	字符串相加，数字相加，列表相加；如果失败，将会返回一个空字符串。--如果是字符串会转换为整数
      default	
      	提供一个默认值，在该值需被django认为是False的时候使用。如：空字符/None。区别于default_if_none,default只有在变量为None时才使用默认值
      first/last
      	返回列表中的第一个/最后一个值
      data
      	格式化日期和时间
      time
      	格式化时间
      join
      	跟python中的join一样的用法
      length
      	返回字符串或者数组的长度
      length_is
      	判断字符串或数组长度是否为指定的值
      lower
      	字符串小写
      truncatechars
      	根据后面的参数，截断字符，超过用...表示
      truncatewords
      	同truncatechars，以单词为单位进行截断。若这些拆分的内容中有html截断标签中的字符，而不会截断标签。
      capfirst
      	首字母大写
      slice
      	切割列表。如同python切片操作
      striptage
      	去掉所有的html标签
      safe
      	关闭变量的自动转义
      floatformat
      	浮点数格式化
      
      
      ```

   3. ![date和time过滤器格式](https://i.loli.net/2021/03/22/D7vXeBAy4WnQd2K.png)

   4. 补充知识点：跨域脚本攻击

      1. 放射性--有即时性
      2. 存储性--有延后性

   

   **静态文件**

   1. 静态文件--CSS，JS，Img
   2. 跟动态文件一样有两种保存方式
   3. 命名为static文件夹
   4. settings.py中静态文件的前缀后添加相关路径
      1. `STATIC_URL = '/static/'`  --静态文件默认路径前缀
      2. 路径添加如下：`STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]`
   5. CSS
      1. 在`static/teacher/css/index.css`中写好样式后，在html中进行导入
      2. 不推荐写法：`<link rel="stylesheet" href="/static/teacher/css/index.css" >`
      3. 推荐写法：`<link rel="stylesheet" href="{% static 'teacher/css/index.css'%}" >` -- 默认静态文件名修改后无需对子文件进行修改

**bootstrap插件**

官网：https://www.bootcss.com/

学习里面的示例

html-->css/...

**注意文件相关！**

## 模板标签

#### 常用模板标签

`{%load static %}`

`{%标签%}{%结束标签%}`

![常用标签](https://i.loli.net/2021/03/23/9BJPhty4lRMANzp.png)
```html
{# 示例如下 #}

<table>
        <tr>
            <th>序号</th>
            <th>姓名</th>
            <th>年龄</th>
            <th>身高</th>
            <th>性别</th>
        </tr>
        {% for student in students %}
            {% with stu_name=student.name %}
                别名：{{ stu_name }}
            {% endwith %}
        <tr {% if student.sex == "女" %}style="color:red"{% endif %}>
            <td><a href="{% url 'teacher:detail' student.name %}">{{ forloop.counter }}</a></td>
            <td>{{ student.name }}</td>
            <td>{{ student.age }}</td>
            <td>{{ student.height }}</td>
            <td>{{ student.sex }}</td>
        </tr>
        {% endfor %}
</table>
```

**注意：**

1. Django框架语法严格，注意不能缺/多空格。
2. 每次在视图上新写程序块都要注意：传参，引用，导入...

#### 模板的继承和引用

##### 引用include

Django模板通过模板标签include实现在一个模板中的特定位置引入另一个模板的内容。

写好引用模板-->在另一模板对应位置进行导入

代码为：

```html
<div id="ad">
    {% include 'teacher/ad.html' %}
</div>
```



##### 继承extends+block

将你想要继承的页面通过`{% extends 'teacher/base.html' %}`（**注意放在第一行**）应用在实际使用的页面上

在继承的页面上使用`{% block content %}{% endblock %}`挖坑，并在应用页面将想要填入继承页面坑中的内容用上述代码库框起。

注：继承后，将之识别继承内容，额外标签可删去。

#### 自定义模板过滤器

```python
"""
例子：
	设置选项型数据时，通常不会直接输入内容（如“男”“女”），而是会选择使用数字（1，0），然后通过模板过滤器在页面上显示为具体数据。
代码布局
	某个app特有；根目录，多app共有
	常用设置为：某个app特有。
步骤
	1.创建名叫包含{_init_.py}tempaltetags的包
	2.app需要在setting.py中的INSTALLED_APPS中配置好app路径，模板文件夹会被自动找寻到。
	3.需要重启服务应用
	4.写好自定义函数过滤器--customer_filter.py
	5.在模板导入刚才的文件
	6.使用，在模板相关参数后添加"|sex1[:'en']" （[]内可选）
"""
	
# customer_filter.py
from django import template
register = template.Library()   # 变量名必须是register

def to_sex(value,flag='zh'):
    change={
        'zh':('女','男'),
        'en':('Female','Male',
    }
    return change[flag][value]

register.filter("sex1",to_sex) # 第一个参数(name)可省，用途为给过滤器重新命名。省去即函数名=过滤器名
	
	
```

#### 自定义标签

##### 简单标签

```python
"""
步骤（类似自定义过滤器）:
	创建文件夹，创建.py文件
	在自定义标签文件(customer_tags.py)中编写函数
	注测--主要区别所在
	使用前导入
	上下文管理--通过context传递到自定义标签
"""
# customer_tags.py
from datetime import datetime
from django.template import Library

register = Library()


@register.simple_tag(name='current', takes_context=True)
def current_time(context):
    return datetime.now().strftime(context['format_str'])
```



##### 包含标签

```
# 一个模板通过渲染另一个模板来展示数据

实现：表格内容显示

步骤：数据写入-->视图嵌入-->优化

视图简单实现：
	1.<td>{{ student.course }}</td>
	2.<td>{% for course in student.course %}{{ course }}{% endfor %}</td>
	3.<td><ul>{% for course in student.course %}<li>{{ course }}</li>{% endfor %}</ul></td>

模板化并优化：
# index.html
<td>{% show_list student.course flag='list' %}</td>	

# customer_tag.py
@register.inclusion_tag('teacher/show_list_as_ul.html', name="show_list")
def show_list_as_ul(value, flag):  # 定义一个函数，接收模板变量
    return {'u_list': value, 'flag': flag}  # 'u_list'由模板决定

# show_list_as_ul.html
{% if flag == 'list' %}
<ul class="list-group">
    {% for item in u_list %}
  <li class="list-group-item">{{ item }}</li>
    {% endfor %}
</ul>

{% elif flag == 'link' %}
<div class="list-group">
    {% for item in u_list %}
  <a href="#" class="list-group-item">{{ item }}</a>
    {% endfor %}
</div>

{% else %}
<div class="list-group">
    {% for item in u_list %}
  <button type="button" class="list-group-item">{{ item }}</button>
    {% endfor %}
</div>
{% endif %}
```

