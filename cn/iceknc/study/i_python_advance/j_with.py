# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/27
# @Desc  : 
"""
上下文管理器
    任何实现了 __enter__() 和 __exit__() 方法的对象都可称之为上下文管理器，上下文
    管理器对象可以使用 with 关键字。显然，文件（file）对象也实现了上下文管理器。

    那么文件对象是如何实现这两个方法的呢？我们可以模拟实现一个自己的文件类，让该类
    实现 __enter__() 和 __exit__() 方法。
"""


def m1():  # 普通版
    f = open("output.txt", "w")
    f.write("python之禅")
    f.close()


def m2():  # 进阶版
    f = open("output.txt", "w")
    try:
        f.write("python之禅")
    except IOError:
        print("oops error")
    finally:
        f.close()


def m3():
    with open("output.txt", "r") as f:
        f.write("Python之禅")


class File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("entering")
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, *args):
        print("will exit")
        self.f.close()


def main():
    m1()
    m2()
    m3()

    with File('out.txt', 'w') as f:
        print("writing")
        f.write('hello, python')


if __name__ == "__main__":
    main()
