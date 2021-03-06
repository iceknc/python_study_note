# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/17
# @Desc  :
"""
numpy中常见的数据类型

+==================+==================+============================================================
|  type            |      type code   |    desc
+------------------+------------------+------------------------------------------------------------
|int8/uint8        |   i1/u1          |有符号和无符号的8位(1字节)整型
+------------------+------------------+------------------------------------------------------------
|int16/uint16      |   i2/u2          |有符号和无符号的16位(2字节)整型
+------------------+------------------+------------------------------------------------------------
|int32/uint32      |   i4/u4          |有符号和无符号的32位(4字节)整型
+------------------+------------------+------------------------------------------------------------
|int64/uint64      |   i8/u8          |有符号和无符号的64位(8字节)整型
+------------------+------------------+------------------------------------------------------------
| float16          |   f2             |半精度浮点数
+------------------+------------------+------------------------------------------------------------
| float32          |   f4 or f        |标准的单精度浮点数，与C的float兼容
+------------------+------------------+------------------------------------------------------------
| float64          |   f8 or d        |标准的双精度浮点数，与C的double和python的float对象兼容
+------------------+------------------+------------------------------------------------------------
| float128         |   f16 or g       |扩展精度浮点数
+------------------+------------------+------------------------------------------------------------
|complex64/128/256 |   c8/c16/c32     |分别用两个32/64/128位浮点数表示的复数
+------------------+------------------+------------------------------------------------------------
| boole            |    ?             |存储True和False值的布尔类型
+==================+==================+=============================================================
"""

import numpy as np
import random


def main():
    a = np.array([1, 2, 3, 4, 5])
    b = np.array(range(1, 6))
    c = np.arange(1, 6)  # 上面一行的简写
    print(c)
    d = np.arange(2, 10, 2)
    print(d)
    print(d.dtype)  # 数据类型
    e = d.astype('f8')  # 修改数据类型
    print(e)
    print(e.dtype)
    f = np.array(range(4, 9), dtype='c8')  # 指定创建的数据类型
    print(f)

    g = np.array([random.random() for i in range(10)])
    print(g)
    h = np.round(g, 4)  # 修改浮点型的小数位数
    print(h)

    print(h.shape)  # 数组的形状
    i = np.array([[1, 2, 3], [4, 5, 6]])
    print(i.shape)

    j = g.reshape(2, 5)  # 修改数组的形状
    print(j)

    k = np.array([i for i in range(24)])
    print(k)
    print(k.reshape((2, 3, 4)))

    print(k.flatten()) #把数组转化为1维数组

if __name__ == "__main__":
    main()
