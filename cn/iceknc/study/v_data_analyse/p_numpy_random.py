# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/24
# @Desc  : 
import numpy as np


def main():
    rand = np.random.rand(2, 3)  #创建给定参数维度的均匀分布的随机数数组，浮点数，范围0~1
    print(rand)
    print('\n')
    randn = np.random.randn(2, 3) #创建给定参数维度的标准正态分布随机数，浮点数，平均值0，标准差1
    print(randn)
    print('\n')
    randint = np.random.randint(0, 10, (5, 7)) #从给定上下限范围内取随机整数，维度由(x,y)指定
    print(randint)
    print('\n')
    uniform = np.random.uniform(0, 10, (5, 6)) #从给定上下限范围内产生均匀分布的数组，浮点数，维度由(x,y)指定
    print(uniform)



if __name__ == "__main__":
    main()
