# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/23
# @Desc  : 
import numpy as np


def main():
    print(type(np.nan))  # not a number
    print(type(np.inf))  # infinity
    print(np.nan == np.nan)  # 两个nan不相等

    t = np.array([[1, 2, 3, np.nan], [4, np.nan, 5, 6]])
    print(t)
    print(np.count_nonzero(t != t))  # 获取数组中nan的个数

    print(np.isnan(t))  # 判断一个数组是否为nan

    # nan和任何值计算都为nan
    # 在一组数据中单纯的把nan替换成0合适吗？
    # 如果替换成0后，替换之前的平均值如果大于0，替换之后的均值肯定会变小，所以更一般的方法是把确实的数据替换成为均值
    # 或者直接删除有缺失值的一行

    t = np.array(
        [[0, 1, 2, 3, 4, 5], [6, 7, np.nan, 9, 10, 11], [12, 13, 14, np.nan, 16, 17], [18, 19, 20, 21, 22, 23]])

    for i in range(t.shape[1]):
        nan_num = np.count_nonzero(t[:, i][t[:, i] != t[:, i]])  # 计算nan的个数
        if nan_num > 0:
            now_col = t[:, i]
            now_col_not_nan = now_col[np.isnan(now_col) == False].sum()
            now_col_mean = now_col_not_nan / (t.shape[0] - nan_num)
            now_col[np.isnan(now_col)] = now_col_mean
            t[:, i] = now_col
    print(t)


if __name__ == "__main__":
    main()
