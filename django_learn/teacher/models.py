# 模型对应的就是类，也即数据库中的表。类属性即字段；实例即数据。

from django.db import models


# Create your models here.
class Student(models.Model):
    num = models.AutoField(primary_key=True)  # 如果不指定自动生成
    name = models.CharField(max_length=20)
    age = models.SmallIntegerField()
    height = models.IntegerField(null=True)
    sex = models.SmallIntegerField(default=1)  # 设置默认值
    qq = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    # c_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)    # 创建时间 自动填充当前时间
    c_time = models.DateTimeField('创建时间', auto_now_add=True)
    x_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name
