from django.contrib import admin
from .models import *

'''
利用django自带的admin后台管理，来增加大类、小类和账户数据
修改admin.py，在admin中注册对应的model
'''

admin.site.register(Currency)
admin.site.register(Account)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(HistoryRecord)
