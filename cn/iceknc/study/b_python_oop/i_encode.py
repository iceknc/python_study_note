"""
Python 2.x 默认使用 ASCII 编码
Python 3.x 默认使用 UTF-8 编码

Python 2.x
    文件的第一行加入 #*-*coding:utf8*-* 编译器就会用utf8编码来编译
    即使指定了文件使用utf8的编码格式，但是在遍历字符串时，仍然会以字节为单位遍历字符串
    要能够正确的遍历字符串，在定义字符串时，需要在字符串的引号前，增加一个小写字母u即可
"""

str = u"hello python, hello 世界"
for s in str:
    print(s)