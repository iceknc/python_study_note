# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/6/3
# @Desc  : 
"""
装饰器功能
    引入日志
    函数执行时间统计
    执行函数前预备处理
    执行函数后清理功能
    权限校验等场景
    缓存
"""

from time import ctime, sleep


# 定义函数：完成包裹数据
def makeBold(fn):
    print("makeBold")

    def wrapped():
        return "<b>" + fn() + "</b>"

    return wrapped


# 定义函数：完成包裹数据
def makeItalic(fn):
    print("makeItalic")

    def wrapped():
        return "<i>" + fn() + "</i>"

    return wrapped


@makeBold
def bold():
    return "hello world-1"


@makeItalic
def italic():
    return "hello world-2"


# 多个装饰器
@makeBold
@makeItalic
def both():
    return "hello world-3"


# 装饰带有参数的函数
def time_func(func):
    print("time_func")

    def wrapped_func(a, b):
        print("%s called at %s" % (func.__name__, ctime()))
        print(a, b)
        func(a, b)

    return wrapped_func


@time_func
def func(a, b):
    print(a + b)


# 装饰有不定长参数的函数
def time_func1(func):
    def wrapped_func(*args, **kwargs):
        print("%s called at %s" % (func.__name__, ctime()))
        # func(args,kwargs) 不行，相当于传递了2个参数：1个元组，1个字段
        func(*args, **kwargs)  # 拆包

    return wrapped_func


@time_func1
def func1(a, b, c):
    print(a + b + c)


# 通用装饰
def time_func2(func):
    def wrapped_func(*args, **kwargs):
        print("%s called at %s" % (func.__name__, ctime()))
        return func(*args, **kwargs)  # 一般情况下为了让装饰器更通用，可以有return

    return wrapped_func


@time_func2
def func2(a, b, c):
    return a + b + c


def time_fun_arg(pre="hello"):
    def time_fun(func):
        def wrapped_func():
            print("%s called at %s %s" % (func.__name__, ctime(), pre))
            return func()
        return wrapped_func
    return time_fun

# 下面的装饰过程
# 1. 调用timefun_arg("itcast")
# 2. 将步骤1得到的返回值，即time_fun返回， 然后time_fun(foo)
# 3. 将time_fun(foo)的结果返回，即wrapped_func
# 4. 让foo = wrapped_fun，即foo现在指向wrapped_func
@time_fun_arg("itcast")
def foo():
    print("I am foo")

@time_fun_arg("python")
def too():
    print("I am too")


#类装饰器
class Test(object):
    def __init__(self, func):
        print("---初始化---")
        print("func name is %s" % func.__name__)
        self.__func = func

    def __call__(self):
        print("---装饰器中的功能---")
        self.__func()


# 说明：
# 1. 当用Test来装作装饰器对test函数进行装饰的时候，首先会创建Test的实例对象
#   并且会把test这个函数名当做参数传递到__init__方法中
#   即在__init__方法中的属性__func指向了test指向的函数
#
# 2. test指向了用Test创建出来的实例对象
#
# 3. 当在使用test()进行调用时，就相当于让这个对象()，因此会调用这个对象的__call__方法
#
# 4. 为了能够在__call__方法中调用原来test指向的函数体，所以在__init__方法中就需要一个实例属性来保存这个函数体的引用
#   所以才有了self.__func = func这句代码，从而在调用__call__方法中能够调用到test之前的函数体
@Test
def test():
    print("----test---")


def main():
    print(bold())
    print(italic())
    print(both())

    print("--" * 20)
    func(3, 5)
    print("--" * 20)
    func1(10, 20, 30)
    print("--" * 20)
    print(func2(40, 50, 60))
    print("--" * 20)
    test()
    print("--" * 20)
    foo()
    print("--" * 20)
    too()


if __name__ == "__main__":
    main()
