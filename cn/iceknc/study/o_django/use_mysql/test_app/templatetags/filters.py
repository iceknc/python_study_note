# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/4
# @Desc  : 
from django.template import Library

# 创建一个Library类对象
register = Library()


# 使用装饰器进行注册
@register.filter
# 定义求余函数mod，将value对2求余
def mod(value):
    return value % 2 == 0
