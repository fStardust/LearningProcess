from students.models import Grade
from django import template

register = template.Library()


@register.inclusion_tag('students/grade_option.html')
def grade_option(value):
    grades = Grade.objects.all()
    return {
        "grades": grades,
        "student": value,
    }


@register.inclusion_tag('students/pagination.html', takes_context=True)
def pagination_html(context):
    total_page = context['total_page']  # 总页码数
    page = int(context['page'])  # 当前页
    num = 1  # 当前页左右显示几页

    page_list = []

    # 第一部分：当前页+左边页码范围
    if page - num <= 0:     # 当前页左边不够显示,页面范围从1到当前页
        for i in range(1, page + 1):
            page_list.append(i)
    else:  # 当前页左边够显示，页码范围从page-num
        for i in range(page - num, page + 1):
            page_list.append(i)

    # 第二部分：右边页面范围
    if page + num >= total_page:    # 当前页左边不够显示,页面范围从当前页+1到total_page
        for i in range(page + 1,  total_page+1):
            page_list.append(i)     # 当前页左边够显示,页面范围从当前页+1到page+num
    else:  # 当前页左边够显示，页码范围从page-num
        for i in range(page + 1,  page + num + 1):
            page_list.append(i)

    return {
        "page_list": page_list,
        "page": page,
        "per_page": context['per_page'],
        "total_page": total_page,

    }


@register.simple_tag()
def add_class(field, class_str):
    return field.as_widget(attrs={'class': class_str})
