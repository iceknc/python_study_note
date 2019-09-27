# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/19
# @Desc  : 
import numpy as np


def main():
    a = np.array([i for i in range(24)]).reshape((3, 8))
    print(a)

    print('--' * 20)
    print(a + 1)

    print('--' * 20)
    print(a * 2)

    print('--' * 20)
    print(a / 0)  # nan: not a number   inf:infinite 无穷

    b = np.array([i + 100 for i in range(24)]).reshape((3, 8))
    print('--' * 20)
    print(b)

    print('--' * 20)
    print(a * b)

    c = np.array([i+2 for i in range(8)])
    print('--' * 20)
    print(c)
    print(a + c)

    d = np.array([i+2 for i in range(3)]).reshape((3,1))
    print('--' * 20)
    print(d)
    print(a + d)

    #如果两个数组的后缘维度的轴长度相符或者其中一方的长度为1，则认为他们是广播兼容的
if __name__ == "__main__":
    main()
