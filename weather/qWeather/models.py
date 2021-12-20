from django.db import models


class Weather(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')



