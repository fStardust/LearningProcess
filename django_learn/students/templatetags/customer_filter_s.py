from django import template

register = template.Library()


@register.filter()
def to_male(value, flag="zh"):
    change = {
        "zh": ("女", "男"),
        "en": ("Female", "Male"),
    }
    return change[flag][value]
