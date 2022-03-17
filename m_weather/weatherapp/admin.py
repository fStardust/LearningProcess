from django.contrib import admin

# Register your models here.
from .models import TrigTime, Condition

admin.site.register(TrigTime)
admin.site.register(Condition)
