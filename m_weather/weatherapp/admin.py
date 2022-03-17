from django.contrib import admin

# Register your models here.
from .models import TrigTime, Condition, Recommend

admin.site.register(TrigTime)
admin.site.register(Condition)
admin.site.register(Recommend)
