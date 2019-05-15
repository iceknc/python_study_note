# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/14
# @Desc  :

"""
匹配单个字符
    . 	 匹配任意1个字符（除了\n）
    [] 	 匹配[]中列举的字符
    \d 	 匹配数字，即0-9
    \D 	 匹配非数字，即不是数字
    \s 	 匹配空白，即 空格，tab键
    \S 	 匹配非空白
    \w 	 匹配单词字符，即a-z、A-Z、0-9、_
    \W 	 匹配非单词字符
"""

import re

def main():
    ret = re.match("t.o", "too")
    print(ret.group())

    # 如果hello的首字符大写，那么正则表达式需要大写的H
    ret = re.match("H", "Hello Python")
    print(ret.group())

    # 大小写h都可以的情况
    ret = re.match("[hH]", "hello Python")
    print(ret.group())
    ret = re.match("[hH]", "Hello Python")
    print(ret.group())
    ret = re.match("[hH]ello Python", "Hello Python")
    print(ret.group())

    # 匹配0到9第一种写法
    ret = re.match("[0123456789]Hello Python", "7Hello Python")
    print(ret.group())

    # 匹配0到9第二种写法
    ret = re.match("[0-9]Hello Python", "7Hello Python")
    print(ret.group())

    # 匹配0到9第三种写法
    ret = re.match("\dHello Python", "8Hello Python")
    print(ret.group())

    ret = re.match("[0-35-9]Hello Python", "7Hello Python")
    print(ret.group())

    # 下面这个正则不能够匹配到数字4，因此ret为None
    ret = re.match("[0-35-9]Hello Python", "4Hello Python")
    #print(ret.group())

    ret = re.match("Hello\wPython", "Hello_Python")
    print(ret.group())
    ret = re.match("Hello\wPython", "Hello啊Python")
    print(ret.group())


if __name__ == "__main__":
    main()
    






