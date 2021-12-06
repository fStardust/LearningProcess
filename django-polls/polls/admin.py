from django.contrib import admin

from .models import Question, Choice


# Register your models here.

# admin.site.register(Choice)   # 低效的添加“选项”的做法，应当在创建“投票”对象时就直接添加“选项”
class ChoiceInline(admin.TabularInline):
    model = Choice
    # extra 控制 3个关联的选项插槽，每次返回任意已创建对象的“修改”页面时，都会创建3个新的插槽
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        # "collapse" 类能显示一些格外的折叠样式来作为初始化样式
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # 这些内容直接显示在列标题上（除了把‘_’换成‘ ’）可以在当前目录中的 models.py 添加 display()装饰器 进行改写
    # 添加好后，在当前类中 添加对应过滤器--list_filter 这样在页面中添加了一个’过滤器‘侧边栏，允许通过pub_date字段 过滤列表
    # 展示的 过滤器类型 取决于你要过滤的 字段类型
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']   # 在列表顶部增加搜索框，搜索question_text字段


admin.site.register(Question, QuestionAdmin)
