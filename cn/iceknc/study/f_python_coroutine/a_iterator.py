# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/14
# @Desc  :

"""
可迭代判断
    from collections.abc import Iterable
    isinstance
迭代器判断
    from collections.abc import Iterator
    isinstance

    可迭代对象的本质就是可以向我们提供一个这样的中间“人”即迭代器帮助我们对其进行迭代遍历使用。

    可迭代对象通过__iter__方法向我们提供一个迭代器，我们在迭代一个可迭代对象的时候，
    实际上就是先获取该对象提供的一个迭代器，然后通过这个迭代器来依次获取对象中的每一个数据.

    同时有 __iter__  跟 __next__ 方法的对象可以认为是一个迭代器对象
"""

from collections.abc import Iterable
from collections.abc import Iterator


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return ClassIterator(self)


class ClassIterator(object):
    def __init__(self, obj):
        self.obj = obj
        self.curr_index = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.curr_index < len(self.obj.names):
            ret = self.obj.names[self.curr_index]
            self.curr_index += 1
            return ret
        else:
            raise StopIteration

class ClassmatePro(object):
    def __init__(self):
        self.names = list()
        self.curr_index = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr_index < len(self.names):
            item = self.names[self.curr_index]
            self.curr_index += 1
            return item
        else:
            raise StopIteration

class FibIterator(object):
    """斐波那契数列迭代器"""
    def __init__(self, n):
        """
        :param n: int, 指明生成数列的前n个数
        """
        self.n = n
        # current用来保存当前生成到数列中的第几个数了
        self.current = 0
        # num1用来保存前前一个数，初始值为数列中的第一个数0
        self.num1 = 0
        # num2用来保存前一个数，初始值为数列中的第二个数1
        self.num2 = 1

    def __next__(self):
        """被next()函数调用来获取下一个数"""
        if self.current < self.n:
            num = self.num1
            self.num1, self.num2 = self.num2, self.num1+self.num2
            self.current += 1
            return num
        else:
            raise StopIteration

    def __iter__(self):
        """迭代器的__iter__返回自身即可"""
        return self

def main():
    data = [1, 2, 3, 4, 5, 6]
    iter_data = iter(data)
    print(isinstance(data, Iterable))
    print(isinstance(iter_data, Iterator))

    classmate = Classmate()
    classmate.add("老王")
    classmate.add("张三")
    classmate.add("李四")
    classmate.add("王五麻子")

    for item in classmate:
        print(item)

    classmate_pro = ClassmatePro()
    classmate_pro.add("laowang")
    classmate_pro.add("zhangsan")
    classmate_pro.add("lisi")
    classmate_pro.add("wangwumazi")

    for item in classmate_pro:
        print(item)

    fib = FibIterator(10)
    for num in fib:
        print(num, end=" ")

if __name__ == "__main__":
    main()
