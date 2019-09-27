# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/17
# @Desc  : 
from matplotlib import pyplot as plt
from matplotlib import font_manager


def main():
    interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]
    width = [5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]
    quantity = [836, 2737, 3723, 3926, 3596, 1438, 3273, 642, 824, 613, 215, 47]

    plt.figure(figsize=(15, 10), dpi=80)

    plt.bar(range(len(interval)), quantity, width=1)

    x = [i - 0.5 for i in range(13)]
    xtick_labels = interval + [150]
    plt.xticks(x, xtick_labels)
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
