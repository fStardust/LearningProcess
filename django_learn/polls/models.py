from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    # 将Question 跟 Choice 关联起来 多对一关系
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)