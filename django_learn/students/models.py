from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField("姓名", max_length=20)
    age = models.SmallIntegerField('年龄', null=True)
    SEX_CHOICE = (
        [0, '女'],
        [1, '男'],
    )
    sex = models.SmallIntegerField('性别', choices=SEX_CHOICE, default=1)
    qq = models.CharField('QQ', max_length=20, unique=True, error_messages={'unique': 'qq号码重复！'})   # 错误提示信息
    phone = models.CharField('电话', max_length=20, unique=True)
    c_time = models.DateTimeField('创建时间', auto_now_add=True)
    # detail = models.OneToOneField('StudentDetail',on_delete=models.SET_NULL,null=True)
    grade = models.ForeignKey('Grade', on_delete=models.SET_NULL, null=True)  # 一对多

    is_delete = models.BooleanField(default=False)  # 设置一个字段来记录数据的状态

    def __str__(self):
        return "{}-{}".format(self.name, self.age)


class StudentDetail(models.Model):
    college = models.CharField('学院', max_length=20)
    student = models.OneToOneField('Student', on_delete=models.CASCADE)

    def __str__(self):
        return self.college


class Grade(models.Model):
    name = models.CharField('班级名称', max_length=20)
    num = models.CharField('年级', max_length=20)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField('课程名称', max_length=20)
    students = models.ManyToManyField('Student', through='Enroll', related_name="courses")

    # 不加through='Enroll'；自动生成中间表--students_course_students;related_name="courses"指定反向模型名

    def __str__(self):
        return self.name


# 指定中间表
class Enroll(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    pay = models.FloatField('缴费金额', default=0)
    c_time = models.DateTimeField('报名时间', auto_now_add=True)
