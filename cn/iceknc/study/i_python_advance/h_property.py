# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/27
# @Desc  :

"""
property属性
    一种用起来像是使用的实例属性一样的特殊属性，可以对应于某个方法

property属性的定义和调用要注意一下几点：
    定义时，在实例方法的基础上添加 @property 装饰器；并且仅有一个self参数
    调用时，无需括号

property属性的有两种方式
    装饰器 即：在方法上应用装饰器
        经典类，具有一种@property装饰器
        新式类，具有三种@property装饰器
            分别对应了三个被@property、@方法名.setter、@方法名.deleter修饰的方法
    类属性 即：在类中定义值为property对象的类属性
        使用类属性的方式创建property属性时，经典类和新式类无区别
            property方法中有个四个参数
            第一个参数是方法名，调用 对象.属性 时自动触发执行方法
            第二个参数是方法名，调用 对象.属性 ＝ XXX 时自动触发执行方法
            第三个参数是方法名，调用 del 对象.属性 时自动触发执行方法
            第四个参数是字符串，调用 对象.属性.__doc__ ，此参数是该属性的描述信息
"""

class Goods(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price

class Foo(object):
    def get_bar(self):
        print("getter...")
        return 'laowang'

    def set_bar(self, value):
        """必须两个参数"""
        print("setter...")
        return 'set value' + value

    def del_bar(self):
        print("deleter...")
        return 'laowang'

    BAR = property(get_bar, set_bar, del_bar, "description...")


def main():
    obj = Goods()
    obj.price  # 获取商品价格
    obj.price = 200  # 修改商品原价
    del obj.price  # 删除商品原价

    obj = Foo()
    obj.BAR  # 自动调用第一个参数中定义的方法：get_bar
    obj.BAR = "alex"  # 自动调用第二个参数中定义的方法：set_bar方法，并将“alex”当作参数传入
    desc = Foo.BAR.__doc__  # 自动获取第四个参数中设置的值：description...
    print(desc)
    del obj.BAR  # 自动调用第三个参数中定义的方法：del_bar方法

if __name__ == "__main__":
    main()
