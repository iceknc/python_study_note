# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/23
# @Desc  : 
import numpy as np


def main():
    a = np.array([i for i in range(12)]).reshape(3, 4)
    print(a)
    print('-**-' * 20, end='\n\n')

    print(a[0])  # 取一行     [起始行:终止行 , 起始列:终止列]
    print('\n')
    print(a[0:2, :])  # 取多行
    print('\n')
    print(a[[0, 1, 2]])
    print('\n')
    print(a[0::2])  # 步长，取单数行
    print('-**-' * 20, end='\n\n')

    print(a[:, 1])  # 取一列
    print('\n')
    print(a[:, 0:2])  # 取多列
    print('-**-' * 20, end='\n\n')

    print(a[1, 2])  # 去第2行第3列的结果
    print('\n')
    print(a[0:2, 0:2])  # 取行列交叉点的位置
    print('-**-' * 20, end='\n\n')

    a[:, 1] = 0
    print(a)  # 修改值
    print('-**-' * 20, end='\n\n')

    print(a < 2)
    print('-**-' * 20, end='\n\n')

    a[a < 2] = 2  # 把小于2的值修改为2
    print(a)
    print('-**-' * 20, end='\n\n')

    print(np.where(a <= 2, 10, 5))  # 三目运算符  小于等于2的替换成10，其他的替换成5
    print('-**-' * 20, end='\n\n')

    print(a)
    print(a.clip(4, 10)) #小于4的替换成4， 大于10的替换成10


if __name__ == "__main__":
    main()
