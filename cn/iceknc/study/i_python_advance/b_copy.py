# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/16
# @Desc  : 

"""
浅拷贝
    对于一个对象的顶层拷贝
    通俗的理解是：拷贝了引用，并没有拷贝内容
深拷贝
    深拷贝是对于一个对象所有层次的拷贝(递归)
"""
import copy


def main():
    # 浅拷贝
    a = [11, 22]
    b = a
    print("a --> %d  b --> %d" % (id(a), id(b)))

    # 浅拷贝，只会复制最顶层那个列表
    a = [11, 22]
    b = [33, 44]
    c = [a, b]
    d = copy.copy(c)
    print("id(c) --> %d  id(d) -->%d c[0] --> %d  d[0] --> %d" % (id(c), id(d), id(c[0]), id(d[0])))

    print("")
    print("#" * 20)
    print("")

    # 深拷贝
    a = [11, 22]
    b = [33, 44]
    c = [a, b]
    d = copy.deepcopy(c)
    print("id(c) --> %d  id(d) -->%d c[0] --> %d  d[0] --> %d" % (id(c), id(d), id(c[0]), id(d[0])))

    # 分片表达式可以赋值一个序列 属于浅拷贝
    a = [11, 22]
    b = [33, 44]
    c = [a, b]
    d = c[:]
    print("id(c) --> %d  id(d) -->%d c[0] --> %d  d[0] --> %d" % (id(c), id(d), id(c[0]), id(d[0])))

    # copy.copy对于可变类型，会进行浅拷贝
    a = [11, 22]
    b = copy.copy(a)
    a.append(33)
    print("(%d)a:%s  ----  (%d)b:%s" % (id(a), str(a), id(b), str(b)))

    # copy.copy对于不可变类型，不会拷贝，仅仅是指向
    a = (11, 22)
    b = copy.copy(a)
    c = copy.deepcopy(a)
    print("(%d)a:%s  ----  (%d)b:%s  ---  (%d)c:%s" % (id(a), str(a), id(b), str(b), id(c), str(c)))

    a = [11, 22]
    b = [33, 44]
    c = (a, b)
    d = copy.copy(c)
    e = copy.deepcopy(c)
    print("(%d)c:%s  ----  (%d)d:%s  ---  (%d)e:%s" % (id(c), str(c), id(d), str(d), id(e), str(e)))
    a.append(55)
    print("(%d)c:%s  ----  (%d)d:%s  ---  (%d)e:%s" % (id(c), str(c), id(d), str(d), id(e), str(e)))


if __name__ == "__main__":
    main()
