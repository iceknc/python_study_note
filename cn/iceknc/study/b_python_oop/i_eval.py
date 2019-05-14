"""
内建函数
    将字符串当成有效的表达式来求值并返回计算结果
    在开发时千万不要使用直接转换input的结果
        __import__('os').system('rm -rf')
"""

print(eval("1+1"))

print(eval("[1, 2, 3, 4]"))