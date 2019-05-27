# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/27
# @Desc  :
"""
__doc__
    表示类的描述信息

__module__
    表示当前操作的对象在那个模块

__class__
    表示当前操作的对象的类是什么

__init__
    初始化方法，通过类创建对象时，自动触发执行

__del__
    当对象在内存中被释放时，自动触发执行,此方法一般无须定义，因为Python是一门高级语言，程序员在使用时无需关
    心内存的分配和释放，因为此工作都是交给Python解释器来执行，所以，__del__的调用是由解释器在进行垃圾回收
    时自动触发执行的

__call__
    对象后面加括号，触发执行

__dict__
    类或对象中的所有属性

__str__
    打印 对象 时，默认输出该方法的返回值

__getitem__、__setitem__、__delitem__
    用于索引操作，如字典。以上分别表示获取、设置、删除数据

__getslice__、__setslice__、__delslice__
    该三个方法用于分片操作，如：列表
"""


class Foo(object):
    """ 描述类信息，这是用于看片的神奇 """

    def __init__(self, name):
        self.name = name
        print("__init__")

    def __call__(self, *args, **kwargs):
        print("__call__")

    def __getitem__(self, key):
        print('__getitem__', key)

    def __setitem__(self, key, value):
        print('__setitem__', key, value)

    def __delitem__(self, key):
        print('__delitem__', key)

    def __getslice__(self, i, j):
        print('__getslice__', i, j)

    def __setslice__(self, i, j, sequence):
        print('__setslice__', i, j)

    def __delslice__(self, i, j):
        print('__delslice__', i, j)


def main():
    print(Foo.__doc__)
    print(Foo.__module__)
    print(Foo.__class__)

    obj = Foo("a")  # 执行 __init__
    obj()  # 执行 __call__

    result = obj['k1']  # 自动触发执行 __getitem__
    obj['k2'] = 'laowang'  # 自动触发执行 __setitem__
    del obj['k1']  # 自动触发执行 __delitem__

    obj[-1:1]  # 自动触发执行 __getslice__
    obj[0:1] = [11, 22, 33, 44]  # 自动触发执行 __setslice__
    del obj[0:2]  # 自动触发执行 __delslice__


if __name__ == "__main__":
    main()
