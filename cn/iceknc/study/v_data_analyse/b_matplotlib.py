# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/12
# @Desc  : 
from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager


# 这个字体设置为全局设置
# font = {'family': 'Microsoft Yahei', 'size': '10'}
# matplotlib.rc("font", **font)


def main():
    plt.figure(figsize=(30, 15), dpi=80)  # 在图像模糊的时候可以传入dpi，让图像更加清晰
    x = range(0, 120)
    y = [random.randint(20, 35) for i in range(120)]
    plt.plot(x, y)

    x_ticks = ["10点{}分".format(i) for i in x if i < 60]
    x_ticks += ["11点{}分".format(i - 60) for i in x if i > 60]

    font = font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc', size=20)
    plt.xticks(x[::5], x_ticks[::5], rotation=45, fontproperties=font)
    plt.xlabel("时间", fontproperties=font)
    plt.ylabel("温度℃", fontproperties=font)
    plt.title("10点到12点每分钟的温度变化情况", fontproperties=font)

    plt.show()


if __name__ == "__main__":
    main()
