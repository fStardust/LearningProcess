# Django·3

[toc]



## 数据库远程连接配置

#### 默认数据库接口

```python
# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

#### 配置MySQL数据库

1. 安装pymysql： `pip install pymysql`  

   - **注意**，要在对印的环境中安装

2. 创建数据库

   - 需要一个可以远程访问的数据库用户

     ```mysql
     # 创建一个管理员用户take账号，密码为taka：
     	CREATE USER 'take'@'%'IDENTIFIED BY 'taka';
     # 给这个用户授予所有远程访问，这个用户主要用于管理整个数据库，备份，还原等操作。
     	GRANT ALL ON *.* TO 'taka'@'%';
     # 使授权立即生效：
     	FLUSH PRIVILEGES；
     ```

   - root不应该开放远程权限

   - 创建数据库

     ```mysql
     show databases;
     create database CRM charset=utf8;
     # 新建用户并给其远程访问与操作CRM的权限
    grant all privileges on CRM.* to 'qwe'@'%' identified by 'qwe';
     flush privileges; # 刷新数据库
     ```
     
     - ```
       DATABASES = {
       	'default': {
       		'ENGINE': 'django.db.backends.mysql',
                    'NAME': 'CRM',  # 数据库名
                    'USER': 'qwe',
                    'PASSWORD': 'qwe',
                    'HOST': '127.0.0.1',
                    'POST': 3306,
       	}
       }
       ```
   - 导入pymysql
   
     ```python
     # __init__.py
     import pymysql
     ```




## 模型基础

#### ORM介绍

<center>Object Relational Mapping对象关系映射</center>

ORM优势：用面向对象的方式,去描述/操作数据库,达到不用编写sql语句对数据库进行增删改查。



1. 模型文件：teacher/models.py

2. 创建模型

   ```python
   class Student(models.Model):
       name = models.CharField(max_length=20)
       age = models.SmallIntegerField()
       sex = models.SmallIntegerField(default=1)   # 设置默认值
       qq = models.CharField(max_length=20)
       phone = models.CharField(max_length=20)
       # c_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)    # 创建时间 自动填充当前时间
       c_time = models.DateTimeField('创建时间', auto_now_add=True)
   ```

3. 激活模型

   1. 注测app--在settings.py INSTALLED_APPS中有对应app

   2. 迁移

      ```
      python manage.py makemigrations teacher	# 指定qpp生成迁移
      python manage.py makemigrations	# 全部模型迁移
      python manage.py sqlmigrate teacher 0001 # 查询原生sql语句，0001是迁移时生成的版本号
      # 完成这些操作并保存更改，但此时还没有对数据库生效
      ```

   3. 迁移生效

      ```mysql
      python manage.py migrate
      python manage.py migrate teacher # 指定app迁移生效
      
      # 迁移生效后
      
      mysql> show tables;
      +----------------------------+
      | Tables_in_CRM              |
      +----------------------------+
      | auth_group                 |
      | auth_group_permissions     |
      | auth_permission            |
      | auth_user                  |
      | auth_user_groups           |
      | auth_user_user_permissions |
      | django_admin_log           |
      | django_content_type        |
      | django_migrations          |
      | django_session             |
      | teacher_student            |
      +----------------------------+
      11 rows in set (0.00 sec)
      
      mysql> desc teacher_student;
      +--------+-------------+------+-----+---------+----------------+
      | Field  | Type        | Null | Key | Default | Extra          |
      +--------+-------------+------+-----+---------+----------------+
      | id     | int(11)     | NO   | PRI | NULL    | auto_increment |
      | name   | varchar(20) | NO   |     | NULL    |                |
      | age    | smallint(6) | NO   |     | NULL    |                |
      | sex    | smallint(6) | NO   |     | NULL    |                |
      | qq     | varchar(20) | NO   |     | NULL    |                |
      | phone  | varchar(20) | NO   |     | NULL    |                |
      | c_time | datetime(6) | NO   |     | NULL    |                |
      +--------+-------------+------+-----+---------+----------------+
      7 rows in set (0.00 sec)
      
      ```

   4. **重点**

      1. 迁移功能是非常强大的
      2. 可以在开发项目是随时更改模型，不需要删除数据库或创建数据表--实时升级数据库而不丢失数据

   5. **总结：三部曲**

      1. 修改/创建模型
      2. 创建迁移`python manage.py makemigrations`
      3. 迁移生效`python manage.py migrate`

#### 数据的增删改查

1. 基本步骤

   ```mermaid
   graph TD
   	A(进入Python交互式界面)-->B(对数据进行增删改查)-->C(检查及保存)
   ```

2. 进入交互式python shell中

   ``` 
   pip install ipython
   python manage.py shell
   ```

3. 增

   ```python shell
   from teacher.models import Student	# 导入模型
   # 第一种方式：需要将创建的对象保存
   s = Student(name="张三",age=25,qq="123456")
   In [3]: s.save()
   
   # 第二种方式：创建空实例，再属性赋值，记得保存对象
   s1 = Student () 
   s1.name = '李四'
   s1.age = 27 
   s1.save()
    
   # 第三种方式：create直接写入数据库
   Student.objects.create(name='王五',age=16)
   
   # 第四种方式：先查找数据库，若无再添加
   s = Student.objects.get_or_create(name='徐六',sex=0,age=16)
   
   ```

4. **查**

   ```python shell
   ## 未添加返回模型时
   
   # 查所有
   in[1]:res = Student.objects.all()
   in[2]:res
   Out[2]: <QuerySet [<Student: Student object (1)>, <Student: Student object (2)>, <Student: Student object (3)>, <Student: Student object (4)>]>
   In [3]: print(res.query)
   SELECT `teacher_student`.`id`, `teacher_student`.`name`, `teacher_student`.`age`, `teacher_student`.`sex`, `teacher_student`.`qq`, `teacher_student`.`phone`, `teacher_student`.`c_time` FROM `teacher_student`
   ## 在后添加[:2]可做切片操作，但不支持负索引
   
   # 查单条。返回对象。如果符合条件的有多个，会报错。
   In [1]: Student.objects.get(pk=1)  # 主键不一定会命名为id。使用pk会自动去查找表的主键。
   Out[1]: <Student: Student object (1)>
   
   # 带条件查询
   In [1]: Student.objects.filter(age=16)
   Out[1]: <QuerySet [<Student: 王五>, <Student: 徐六>]>   
   ## 排除查询，与fuilter用法相反
   In [1]: Student.objects.exclude(name="lily")
   Out[1]: <QuerySet [<Student: Lucy>, <Student: zhangsan>, <Student: lisi>, <Student: 刘五>, <Student:三>, <Student: 李四>]>
   
   # 查询第一条数数据 --最后一条数据为last 
   In [1]: Student.objects.first()
   Out[1]: <Student: Lucy>
   
   # 指定字段的查询
   ## 只能获得指定字段的值
   In [19]: Student.objects.values('name')
   Out[19]: <QuerySet [{'name': 'Lucy'}, {'name': 'zhangsan'}, {'name': 'lisi'}, {'name': '刘五'}, {'nam: '张三'}, {'name': '李四'}]>
   In [20]: res = Student.objects.values('name')
   In [22]: res[2]['name']
   Out[22]: 'lisi'
   ## 可获得其他指定字段的值
   In [23]: res = Student.objects.only('name')
   In [24]: res
   Out[24]: <QuerySet [<Student: Lucy>, <Student: zhangsan>, <Student: lisi>, <Student: 刘五>, <Student:三>, <Student: 李四>]>
   In [25]: res[2].name
   Out[25]: 'lisi'
   In [26]: res[2].sex 
   Out[26]: 1
   ### defer：与only相反 
   
   ## 想要显示数据 要在原模型后添加如下内容。记得迁移
   # models.py-class Student()
       def __str__(self):
           return self.name
           
   
   ```

5. 改

   ```python shell
   # 第一种方式：修改一条数据
   In [13]: s = Student.objects.get(pk=4) 
   In [14]: s
   Out[14]: <Student: 徐六>
   In [15]: s.phone="123457" 
   In [16]: s.save()
   
   # 第二种方式：修改多条数据
   In [1]: Student.objects.filter(age=25).update(qq="0123456") 
   Out[1]: 2  # 返回值是修改的数据条数
   
   
   ```

6. 删

   ```python
   # 删一条
   In [1]: s = Student.objects.get(pk=3)
   In [2]: s.delete()
   Out[3]: (1, {'teacher.Student': 1})
   
   # 删多条
   In [1]: Student.objects.filter(age=18).delete()
   
   # 全删
   In [1]: Student.objects.all().delete()
   
   
   ```

7. 返回对应sql语句

   ```python shell
   # 将模型相关命令赋给一个参数，打印参数，即可。
   # 举例 在shell界面中
   In [1]: res = Student.objects.all()
   In [2]: print(res.query)
   SELECT `teacher_student`.`num`, `teacher_student`.`name`, `teacher_student`.`age`, `teacher_student`.`height`, `teacher_student`.`sex`, `teacher_student`.`qq`, `teacher_student`.`phone`, `teacher_student`.`c_time`, `teacher_student`.`x_time` FROM `teacher_student`
   ```

8. 补充

   ```
   # 共同点
   都是通过objects去实现的-->objects：每个django模型类都有的一个默认管理类。
   
   # 视图修改 
   # 传数据无需在视图文件上完整输入，可以通过对数据库的增删，修改内容
   # views.py
   sts = Student.objects.all() # 获取相关模型
   ```



#### 查询条件

1. 排序

   ```python shell
   # order_by 根据指定字段排序
   ## 正序
   In [1]: res = Student.objects.order_by('age')
   ## 反序
   In [2]: res = Student.objects.order_by('-age')
   ### 不修改数据库内容，只对输出做排序
   
   
   # 多条件查询
   ## 需要导入库，如下
   In [33]: from django.db.models import Q
   In [36]: Student.objects.filter(Q(sex=1),Q(age=18)|Q(age=12)) 
   Out[36]: <QuerySet [<Student: lisi>, <Student: 刘五>, <Student: 张三>]>
   ```

2. 单filter

   ```python
   # 模糊查询--不区分大小写
   Student.objects.filter(name__iexact="lucy")
   # 精准查询
   Student.objects.filter(name__exact="lucy")
   
   # 精准包含匹配
   Student.objects.filter(name__contains="l")
   
   # 模糊包含匹配--不区分大小写
   Student.objects.filter(name__contains="l")
   
   # 指定值--in__可以列表、元组、文本等方式取值
   Student.objects.filter(pk__in=[1,3,4])
   Student.objects.filter(sex__in="01")
   
   ```

3. 子查询

   ```python shell
   In[1]: res = Student.objects.filter(name__icontains='l').only("name")
   In[2]: res1 = Student.objects.filter(pk__in=res).only("name")
   
   # 原SQL语句-->
   SELECT `teacher_student`.`num`, `teacher_student`.`name` FROM `teacher_student` WHERE `teacher_student`.`num` IN (SELECT U0.`num` FROM `teacher_student` U0 WHERE U0.`name` LIKE %l%)
   ```

4. 大小于 及 范围查询

   ```
   # 以等于为例
   Student.objects.filter(pk__gt=2)
   
   # 范围查询
   res = Student.objects.filter(age__range=(18,30))
   
   
   ```

5. 聚合分组

   ```
   # annotate --分组
   res = Student.objects.values('sex').annotate(ren=Count('sex'))
   ```



## 表关系及相关操作

### 表关系

<center><font color="red">类别：一对一，一对多，多对多</font></center>

<center>表关系字段设置原则：怎么方便怎么来</center>

  <center>例：从学生找班级比从班级找学生更方便-->设在学生表中</center>

![表关系](https://i.loli.net/2021/04/08/Wg4ULuibPpGzEXk.png)

1. One To One

   ```
   OneToOneField
   # 关联语句--可以在两张相关表中任选其一
   student = models.OneToOneField('Student',on_delete=models.CASCADE)
   ## on_delete=models.CASCADE  是指关联表删除后的操作，此处是指*同时删除*
   ```

2. One To Many

   ```
   ForeignKey
   # 关联语句--可以在两张相关表中任选其一..选择多表
   grade = models.ForeignKey('Grade',on_delete=models.SET_NULL,null=True)
   ```

3. Many  To Many

   ```
   ManyToManyField
   # 在模型中无须设置中间表，迁移时会自动生成。
   
   # 指定中间表--表关系语句中需要添加through='Enroll'
   
   ```

4. 回滚

   ```
   回滚到0001版本
   python manage.py migrate students 0001
   注意：回滚后删除其后一个迁移文件，此处指0002
   ```

### 表关系操作

#### 1.一对多 操作（正向/反向）

##### 正向

   ```python
   # 正向：一个模型有外键字段，通过这个模型对外键进行操作就叫正向
   class Student(models.Model):
   	...
   	grade = models.ForeignKey('Grade', on_delete=models.SET_NULL, null=True) 
   	## ↑此句联系Student跟Grade两张表。此句在Student中，通过Student操作的方向为正向
   
   # 正向操作跟普通操作相同
   
   ```

######  增

```python shell

In [2]: g1 = Grade.objects.create(name="django",num="21")
# 属性赋值
In [10]: s1 = Student(name="刘四",age=16,sex=0,qq="123",phone="456",grade=g1) # 其中grade=g1便是将Grade表相关字段联系起来
In [11]: s1.save() # 通过类实例保存的必须有这一步

# 通过主键赋值
In [13]: s2 = Student(name="张三",age=16,qq="223",phone="156")
In [14]: s2.grade_id = g2.id
```

###### 查

```python shell
In [17]: s1.grade
Out[17]: <Grade: Grade object (1)>

In [18]: s1.grade.name
Out[18]: 'django'

In [19]: Student.objects.filter(grade__name="django")
Out[19]: <QuerySet [<Student: 刘四-16>]>
```

###### 删

```python shell
# 将s2从原先班级表中删除
In [21]: s2.grade = None
In [22]: s2.save()
```

##### 反向

```python
# 反向:一个模型如果被另一个模型外键关联，通过这个模型对关联它的模型进行操作叫作反向
class Student(models.Model):
   	...
   	grade = models.ForeignKey('Grade', on_delete=models.SET_NULL, null=True) 
## ↑此句联系Student跟Grade两张表。此句在Student中，通过Grade操作的方向为反向
    
# 操作原理：如果一个模型(eg:Student)有一个ForeignKey(grade)，那么这个外键模型的实例(eg:g1)将可以返回一个Student模型的所有实例的管理器(student_set)(其中的student是模型名，小写)
```

###### 增

```python shell
# 通过student——set管理器
In [23]: new_s = g2.student_set.create(name="李四",age=19,qq="342",phone="2341")
    
# 一次多数据
In [25]: s1,s2,s3 = Student.objects.filter(id__lte=3)
In [26]: g1.student_set.add(s1,s2,s3)
```

###### 改

```python shell
# 增方法也同样可以实现改效果
In [29]: g2.student_set.set([s2,s3])
```

###### 删

```python shell
# 选删
In [30]: g2.student_set.remove(s2,s3)

# 全删
In [32]: g2.student_set.clear()
```

###### 查

```python shell
# 和objects操作一样
In [33]: g1.student_set.all()
Out[33]: <QuerySet [<Student: 刘四-16>]>

In [34]: g1.student_set.filter(age=16)
Out[34]: <QuerySet [<Student: 刘四-16>]>
```

#### 2.多对多操作

```python
class Course(models.Model):
    ...
    students = models.ManyToManyField('Student', through='Enroll',related_name="courses")
    
反向模型管理器：course_set
可以通过related_name来指定属性(courses)替代course_set
```

###### 增

```python shell
In [2]: c1 = Course.objects.create(name="python")
In [3]: s1 = Student.objects.first()
In [5]: e = Enroll()
In [6]: e.course = c1
In [7]: e.student = s1
In [8]: e.save()
```

###### 查

```python shell
# 正向
In [9]: c1.students.all()
Out[9]: <QuerySet [<Student: 刘四-16>]>
# 反向
In [10]: s1.courses.all()
Out[10]: <QuerySet [<Course: Course object (1)>]>
```

#### 3.一对一操作

```python
class StudentDetail(models.Model):
    ...
    student = models.OneToOneField('Student', on_delete=models.CASCADE)

# 正向：一对一字段所在的模型，通过这个模型去访问关联的模型为正向。

```

###### 增

```python shell
# 正向
In [11]: d1 = StudentDetail(college="武汉大学") 
In [12]: d1.student=s1 
In [13]: d1.save()
    
# 反向 之前反向都通过了管理器
## 此处反向类似正向
In [15]: s = Student(name="王五",age=16,sex=0,qq="1232",phone="2312")
In [16]: s.studentdetail = d1 
In [17]: s.save()
```

###### 查

```python shell
# 正向 类似上述
In [14]: StudentDetail.objects.values('college','student__name','student__qq')
Out[14]: <QuerySet [{'college': '武汉大学', 'student__name': '刘四', 'student__qq': '123'}]>

# 反向 之前反向都通过了管理器
## 此处反向类似正向
In [18]: Student.objects.values('name','qq','studentdetail__college')
```

#### 跨表查询

```python shell
# 要跨越关系，只需要跨模型的相关字段的字段名，以双下划线隔开，直到达到想要的结果为止。
# ↓含义：男生报名的课程
In [40]: Course.objects.filter(students__sex=1)
# ↓含义：报名python的学生
In [41]: Student.objects.filter(courses__name="python")
Out[41]: <QuerySet [<Student: 刘四-16>, <Student: 张三-16>, <Student: 李四-19>]>
# ↓含义：报名python的学生，及年级为21
In [42]: Student.objects.filter(courses__name="python",grade__num__contains="21") 
Out[42]: <QuerySet [<Student: 刘四-16>, <Student: 张三-16>, <Student: 李四-19>]>
   
# ↓含义：查询缴费金额小于3000的学生--在中间标中
In [50]: Student.objects.filter(enroll__pay__lt=3000)
    
# ↓含义：学生报名课程的班级有哪些
In [3]: Grade.objects.filter(student__courses__name="python") 
Out[3]: <QuerySet [<Grade: django>, <Grade: django>, <Grade: python>]>
In [4]: Grade.objects.filter(student__courses__name="python").distinct()	# 去重
Out[4]: <QuerySet [<Grade: django>, <Grade: python>]>
```





## Django字段补充

#### Django字段类型与属性

![常用得字段类型映射关系](https://i.loli.net/2021/04/06/FBQIjKbSMGXgvlL.png)

![常用字段类型说明](https://i.loli.net/2021/04/06/K3JjvkfCFean9uB.png)

![Field常用参数](https://i.loli.net/2021/04/06/q8cKd4lLIhW2Raz.png)

注意：其中部分参数无法随时更改。例如一开始未指定`primary_key`，那在表中添加数据后无法在模型中修改/生效。

官方文档：[字段类型](https://docs.djangoproject.com/en/2.1/ref/models/fields/#field-types) & [字段参数](https://docs.djangoproject.com/en/2.1/ref/models/fields/#field-options) 





