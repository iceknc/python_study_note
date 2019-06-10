# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/6/10
# @Desc  :
"""
元类就是用来创建类的“东西”。
元类就是用来创建这些类（对象）的，元类就是类的类
type可以接受一个类的描述作为参数，然后返回一个类。
type(类名, 由父类名称组成的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)

__metaclass__属性
    你可以在定义一个类的时候为其添加__metaclass__属性
    class Foo(object):
    __metaclass__ = something…
    ...省略...
    如果你这么做了，Python就会用元类来创建类Foo 小心点，这里面有些技巧。你首先写下class Foo(object)，
    但是类Foo还没有在内存中创建。Python会在类的定义中寻找__metaclass__属性，如果找到了，
    Python就会用它来创建类Foo，如果没有找到，就会用内建的type来创建这个类。
    当你写如下代码时 :
    class Foo(Bar):
        pass
    Python做了如下的操作：
        Foo中有__metaclass__这个属性吗？如果是，Python会通过__metaclass__创建一个名字为Foo的类(对象)
        如果Python没有找到__metaclass__，它会继续在Bar（父类）中寻找__metaclass__属性，并尝试做和前面同样的操作。
        如果Python在任何父类中都找不到__metaclass__，它就会在模块层次中去寻找__metaclass__，并尝试做同样的操作。
        如果还是找不到__metaclass__,Python就会用内置的type来创建这个类对象。
    现在的问题就是，你可以在__metaclass__中放置些什么代码呢？答案就是：可以创建一个类的东西。那么什么可以用来创建一个类呢？
    type，或者任何使用到type或者子类化type的东东都可以。

究竟为什么要使用元类？
    “元类就是深度的魔法，99%的用户应该根本不必为此操心。如果你想搞清楚究竟是否需要用到元类，那么你就不需要它。
    那些实际用到元类的人都非常清楚地知道他们需要做什么，而且根本不需要解释为什么要用元类。”
                                                                        —— Python界的领袖 Tim Peters
"""


def eat(self):
    print(self.name + "  eat")


@staticmethod
def static_method():
    print("static_method")

@classmethod
def clazz_method(cls):
    print("clazz_method")

def upper_attr(class_name, class_parents, class_attr):
    # class_name 会保存类的名字 Foo
    # class_parents 会保存类的父类 object
    # class_attr 会以字典的方式保存所有的类属性
    new_attr = {}
    for name,value in class_attr.items():
        if not name.startswith("__"):
            new_attr[name.upper()] = value
    # 调用type来创建一个类
    return type(class_name, class_parents, new_attr)

class Foo(object, metaclass=upper_attr):
    # __metaclass__ = upper_attr  # 设置Foo类的元类为upper_attr  python2的用法
    bar = "bip"

class UpperAttrMetaClass(type):
    # __new__ 是在__init__之前被调用的特殊方法
    # __new__是用来创建对象并返回之的方法
    # 而__init__只是用来将传入的参数初始化给对象
    # 你很少用到__new__，除非你希望能够控制对象的创建
    # 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
    # 如果你希望的话，你也可以在__init__中做些事情
    # 还有一些高级的用法会涉及到改写__call__特殊方法，但是我们这里不用
    def __new__(cls, class_name, class_parents, class_attr):
        # 遍历属性字典，把不是__开头的属性名字变为大写
        new_attr = {}
        for name, value in class_attr.items():
            if not name.startswith("__"):
                new_attr[name.upper()] = value

        # 方法1：通过'type'来做类对象的创建
        return type(class_name, class_parents, new_attr)

        # 方法2：复用type.__new__方法
        # 这就是基本的OOP编程，没什么魔法
        # return type.__new__(cls, class_name, class_parents, new_attr)

class Fooo(object, metaclass=UpperAttrMetaClass):
    bar = "bip"

# python2的用法
# class Fooo(object):
#     __metaclass__ = UpperAttrMetaClass
#     bar = 'bip

def main():
    MyDogClass = type("MyDog",
                      (object,),
                      {"name": "Tom", "sex": 1, "eat": eat, "static_method": static_method,"clazz_method":clazz_method})
    print(MyDogClass.__dict__)
    print(help(MyDogClass))


    dog = MyDogClass()
    dog.clazz_method()
    dog.static_method()
    dog.eat()

    f = Foo()
    print(f.BAR)

    fo = Fooo()
    print(fo.BAR)


if __name__ == "__main__":
    main()
