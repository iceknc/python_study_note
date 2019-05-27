# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/20
# @Desc  : 


class Parent(object):
    def __init__(self, name):
        print('parent的init开始被调用')
        self.name = name
        print('parent的init结束被调用')

class Son1(Parent):
    def __init__(self, name, age):
        print('Son1的init开始被调用')
        self.age = age
        Parent.__init__(self, name)
        print('Son1的init结束被调用')

class Son2(Parent):
    def __init__(self, name, gender):
        print('Son2的init开始被调用')
        self.gender = gender
        Parent.__init__(self, name)
        print('Son2的init结束被调用')

class Grandson(Son1, Son2):
    def __init__(self, name, age, gender):
        print('Grandson的init开始被调用')
        Son1.__init__(self, name, age)  # 单独调用父类的初始化方法
        Son2.__init__(self, name, gender)
        print('Grandson的init结束被调用')

def main():
    gs = Grandson('grandson', 12, '男')
    print('姓名：', gs.name)
    print('年龄：', gs.age)
    print('性别：', gs.gender)


if __name__ == "__main__":
    main()
    






