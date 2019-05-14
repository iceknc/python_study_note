"""
模块是python程序架构的一个核心概念
from xxx import yyy
每一个以扩展名py结尾的python源代码都是一个模块

pyc文件
    python解释器将import的模块源码转换为字节码文件，优化速度
"""
from array import ArrayType as at

a = at("b")
print(a)
