# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/16
# @Desc  : 
from matplotlib import pyplot as plt
from matplotlib import font_manager


def main():
    x = ["猩球崛起3：终极之战", "敦刻尔克", "蜘蛛侠：英雄归来", "战狼2"]

    y_1 = [15746, 312, 4497, 319]
    y_2 = [12357, 156, 2045, 168]
    y_3 = [2358, 399, 2358, 362]

    plt.figure(figsize=(30, 20), dpi=40)
    font = font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc', size=20)

    bar_width = 0.2
    x_1 = list(range(len(x)))
    x_2 = [i + bar_width for i in x_1]
    x_3 = [i + bar_width for i in x_2]

    plt.bar(x_1, y_1, width=bar_width, color='orange')
    plt.bar(x_2, y_2, width=bar_width, color='green')
    plt.bar(x_3, y_3, width=bar_width, color='red')

    plt.xticks(x_2, x, fontproperties=font)
    # plt.legend(prop=font, loc='upper right')  # 显示图例 loc = '' 位置

    plt.show()


if __name__ == "__main__":
    main()
