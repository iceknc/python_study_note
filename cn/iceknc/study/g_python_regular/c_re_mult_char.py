# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/14
# @Desc  : 
"""
匹配多个字符的相关格式
    * 	    匹配前一个字符出现0次或者无限次，即可有可无
    + 	    匹配前一个字符出现1次或者无限次，即至少有1次
    ? 	    匹配前一个字符出现1次或者0次，即要么有1次，要么没有
    {m} 	匹配前一个字符出现m次
    {m,n} 	匹配前一个字符出现从m到n次
"""
import re


def main():
    ret = re.match("[A-Z][a-z]*", "M")
    print(ret.group())

    ret = re.match("[A-Z][a-z]*", "MnnM")
    print(ret.group())

    ret = re.match("[A-Z][a-z]*", "")
    print(ret)

    print("=" * 20)
    names = ["name1", "_name", "2_name", "__name__"]

    for name in names:
        ret = re.match("[a-zA-Z_]+[\w]*", name)
        if ret:
            print("变量名 %s 符合要求" % ret.group())
        else:
            print("变量名 %s 非法" % name)

    print("=" * 20)
    ret = re.match("[1-9]?[0-9]", "7")
    print(ret.group())

    ret = re.match("[1-9]?\d", "33")
    print(ret.group())

    ret = re.match("[1-9]?\d", "09")
    print(ret.group())

    print("=" * 20)
    ret = re.match("[a-zA-Z0-9_]{6}", "12a3g45678")
    print(ret.group())

    ret = re.match("[a-zA-Z0-9_]{8,20}", "1ad12f23s34455ff66")
    print(ret.group())

    print("=" * 20)
    ret = re.match(".*", "adsf\nasdfg\ndasfd\nasdfa")
    print(ret.group())

    ret = re.match(".*", "adsf\nasdfg\ndasfd\nasdfa", re.S)
    print(ret.group())


if __name__ == "__main__":
    main()
