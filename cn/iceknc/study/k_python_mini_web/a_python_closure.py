# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/31
# @Desc  : 
"""
闭包
    在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，那么将这个函数以及用到的一些变量称之为闭包


函数、匿名函数、闭包、对象 当做实参时，有什么区别
    匿名函数能够完成基本的简单功能，传递是这个函数的引用 只有功能
    普通函数能够完成较为复杂的功能，传递是这个函数的引用 只有功能
    闭包能够将较为复杂的功能， 传递是这个闭包中的函数以及数据，因此传递的是功能+数据
    对象能够完成较为复杂的功能， 传递是很多数据+很多功能，因此传递的是功能+数据
"""


def test(number):
    def test_in(number_in):
        print("in test_in 函数, number_in is %d" % number_in)
        return number + number_in

    return test_in


def main():
    ret = test(20)
    print(ret(50))


if __name__ == "__main__":
    main()
