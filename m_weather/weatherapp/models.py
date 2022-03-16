from django.db import models


# Create your models here.
class TrigTime(models.Model):
    Trig_time_hour = models.CharField(max_length=10)
    Trig_time_min = models.CharField(max_length=10)
    run_time = models.DateTimeField()
    mod_date = models.DateTimeField('修改日期', auto_now_add=True)

    class Meta:
        verbose_name = "Triggering Time"
        verbose_name_plural = verbose_name


class LogSheet(models.Model):
    run_time = models.ForeignKey(TrigTime, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    correction = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Log Sheet"
        verbose_name_plural = verbose_name
