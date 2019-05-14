# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/14
# @Desc  : 

"""
利用迭代器，我们可以在每次迭代获取数据（通过next()方法）时按照特定的规律进行生成。
但是我们在实现一个迭代器时，关于当前迭代到的状态需要我们自己记录，进而才能根据当前
状态生成下一个数据。为了达到记录当前状态，并配合next()函数进行迭代使用，我们可以采
用更简便的语法，即生成器(generator)
生成器是一个特殊的迭代器
简单来说：只要在def中有yield关键字的 就称为 生成器
"""


def create_num(all_num):
    print("---------------start--------------")
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        print("---------------yield before--------------")
        send = yield a
        print("---------send %s------------" % send)
        a, b = b, a + b
        current_num += 1
        print("---------------yield after--------------")
    return "end ..."  # 返回值会在 StopIteration 的value里面


def main():
    g = [x ** 2 for x in range(20)]
    print(g)

    num = create_num(5)
    for item in num:
        print(item)

    num = create_num(10)
    while True:
        try:
            item = next(num)
            print(item)
        except StopIteration as e:
            print(e.value)
            break

    num = create_num(2)
    ret = next(num)
    print(ret)
    ret = num.send("from send xxxxx")
    print(ret)


if __name__ == "__main__":
    main()
