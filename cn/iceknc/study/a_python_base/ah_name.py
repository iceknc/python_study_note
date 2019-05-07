"""
标示符：变量名、函数名
    可以是：字母、下划线、数字
    不能数字开头
    不能与关键字重名
         关键字: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def',
         'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
         'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

    变量名规则
        每个单词必须是小写字母
        单词间用下划线 _ 链接
    驼峰命名法（非官推）
        大驼峰 全部单词的首字母大写
        小驼峰 除首单词外其他单词首字母大写
"""

import keyword
print(keyword.kwlist)