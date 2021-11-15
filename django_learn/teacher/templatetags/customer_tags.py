from datetime import datetime
from django.template import Library
from django.template.loader import get_template

register = Library()


@register.simple_tag(name='current', takes_context=True)
def current_time(context):
    return datetime.now().strftime(context['format_str'])


# register.simple_tag(current_time, name='current')


@register.inclusion_tag('teacher/show_list_as_ul.html', name="show_list")
def show_list_as_ul(value, flag):  # 定义一个函数，接收模板变量
    return {'u_list': value, 'flag': flag}  # 'u_list'由模板决定

# t = get_template('teacher/show_list_as_ul.html')    # 模板渲染
# register.inclusion_tag(t)(show_list_as_ul)
