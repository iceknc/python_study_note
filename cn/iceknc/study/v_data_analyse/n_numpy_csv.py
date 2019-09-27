# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/20
# @Desc  :
"""
np.loadtxt(fname,dtype=np.float,delimiter=None,skiprows=0,usecols=None,unpack=False)
    fname: 文件、字符串或产生器，可以是.gz或者.bz2压缩文件
    dtype：数据类型，可选，csv的字符串以什么数据类型读入数据中，默认np.float
    delimiter：分隔字符串，默认是任何空格
    skiprows：跳过前x行，一般跳过第一行表头
    usecols：读取指定的列，索引，元祖类型
    unpack：如果True，读入属性将分别写入不同数据变量，False读入数据只写入一个数组变量，默认false
"""
import numpy as np


def main():
    t1 = np.loadtxt('./database/starcraft.csv', delimiter=',', skiprows=1, dtype=str)
    print(t1)

    print("*" * 28)
    print(t1.transpose())

    print("*" * 28)
    print(t1.T)

    print("*" * 28)
    print(t1.swapaxes(1, 0))


if __name__ == "__main__":
    main()
