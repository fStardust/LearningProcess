from django import template

register = template.Library()  # 变量名必须是register

# @register.filter(name="sex1")
@register.filter()
def to_sex(value, flag='zh'):
    change = {
        'zh': ('女', '男'),
        'en': ('Female', 'Male'),
    }
    return change[flag][value]


# register.filter(to_sex)
