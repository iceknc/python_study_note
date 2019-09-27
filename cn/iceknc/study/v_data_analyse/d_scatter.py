# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/16
# @Desc  : 
from matplotlib import pyplot as plt
from matplotlib import font_manager


def main():
    y_3 = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22,
           22,
           22, 23]
    y_10 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11,
            13,
            12, 13, 6]

    plt.figure(figsize=(30, 20), dpi=40)
    font = font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc', size=20)

    x_3 = range(1, 32)
    x_10 = range(51, 82)

    plt.scatter(x_3, y_3, label = '三月份')
    plt.scatter(x_10, y_10, label = '十月份')

    x = list(x_3) + list(x_10)
    x_label = ["3月{}日".format(i) for i in x_3]
    x_label += ["10月{}日".format(i-50) for i in x_10]
    plt.xticks(x[::3], x_label[::3], fontproperties=font,rotation = 45)
    plt.legend(prop=font, loc='upper right')  # 显示图例 loc = '' 位置

    plt.show()


if __name__ == "__main__":
    main()
