# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/23
# @Desc  : 
import numpy as np


def main():
    a = np.array([i for i in range(24)]).reshape(4, 6)
    print(a)
    print('\n')
    print(a.sum())  # 求和
    print('\n')
    print(a.sum(axis=0))  # 求指定轴上的和
    print('\n')
    print(a.mean())  # 均值
    print('\n')
    print(np.median(a))  # 中值
    print('\n')
    print(a.max())  # 极值
    print(np.argmax(a)) # 极值
    print('\n')
    print(a.min())  # 极值
    print(np.argmin(a)) # 极值
    print('\n')
    print(np.ptp(a))  # 极值差
    print('\n')
    print(a.std())  # 标准差

    print('\n')
    zeros_data = np.zeros((a.shape[0], 1)).astype(int) #创建一个全为0的数组
    new_a = np.hstack((a, zeros_data))  # 水平拼接
    print(new_a)

    print('\n')
    ones_data = np.ones((1, a.shape[1])).astype(int) #创建一个全为1的数组
    new_a = np.vstack((a, ones_data))  # 竖直拼接
    print(new_a)

    print('\n')
    t = np.arange(12, 24).reshape(3, 4)
    print(t)
    t[[1, 2], :] = t[[2, 1], :]  # 行交换
    print(t)
    t[:, [0, 1]] = t[:, [1, 0]]
    print(t)  # 列交换

    print('\n')
    print(np.eye(5)) #创建一个对角线为1的正方形数组

if __name__ == "__main__":
    main()
