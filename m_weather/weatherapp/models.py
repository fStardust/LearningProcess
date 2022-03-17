from django.db import models


# Create your models here.
class TrigTime(models.Model):
    trig_time_hour = models.CharField(max_length=8, default="8")
    trig_time_min = models.CharField(max_length=8, default="30")
    mod_date = models.DateTimeField('修改日期', auto_now_add=True)

    class Meta:
        verbose_name = "Triggering Time"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.trig_time_hour, self.trig_time_min


class LogSheet(models.Model):
    run_time = models.DateTimeField()   # 激活时间
    choice_text = models.CharField(max_length=200)      # 建议记录

    class Meta:
        verbose_name = "Log Sheet"
        verbose_name_plural = verbose_name


class Condition(models.Model):
    # log_sheet = models.ForeignKey(LogSheet, on_delete=models.CASCADE)     # 一对多关系
    correction = models.IntegerField(default=0)     # 反馈分数
    self_index = models.IntegerField(default=0)   # 个人指标

    class Meta:
        verbose_name = "Condition"
        verbose_name_plural = verbose_name


class Recommend(models.Model):
    rec_data = models.CharField(max_length=200)
    all_index = models.IntegerField(default=100)

    class Meta:
        verbose_name = "Recommend"
        verbose_name_plural = verbose_name
