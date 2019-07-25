# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/7/23
# @Desc  : 
"""
bytes
    bytes对象只负责以二进制字节序列的形式记录所需记录的对象，至于该对象到底表示什么（比如到底是什么字符）
    则由相应的编码格式解码所决定

Python2 中
    type(b'xxxxx')  -->  <type 'str'>
    type('xxxxx')  -->  <type 'str'>

Python3 中
    type(b'xxxxx')  -->  <class 'bytes'>
    type('xxxxx')  -->  <class 'str'>

bytes是Python 3中特有的，Python 2 里不区分bytes和str。
    python3中：
        str 使用encode方法转化为 bytes
        bytes通过decode转化为str
在Python 2中由于不区分str和bytes所以可以直接通过encode()和decode()方法进行编码解码。
而在Python 3中把两者给分开了这个在使用中需要注意。实际应用中在互联网上是通过二进制进行传输，
所以就需要将str转换成bytes进行传输，而在接收中通过decode()解码成我们需要的编码进行处理数据这样不管对方是
什么编码而本地是我们使用的编码这样就不会乱码。

bytearray
    bytearray和bytes不一样的地方在于，bytearray是可变的。
"""

def main():
    str1 ='人生苦短，我用Python!'

    b1 = bytearray(str1.encode())
    print(b1)

    print(b1.decode())

    b1[:6] = bytearray('生命'.encode())
    print(b1)

    print(b1.decode())


if __name__ == "__main__":
    main()
    






