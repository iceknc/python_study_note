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
    y1 = [random.randint(20, 35) for i in range(120)]
    y2 = [random.randint(20, 35) for i in range(120)]
    y3 = [random.randint(20, 35) for i in range(120)]
    plt.plot(x, y1, label="广东", color='#ff0000', linestyle=':')
    plt.plot(x, y2, label="湖南", color='#00ff00', linestyle='--')
    plt.plot(x, y3, label="辽宁", color='#0000ff', linestyle='-.')
    """
    plt.plot(
        x, #x
        y, #y
        在绘制的时候指定即可
        color = 'r'         r:红色 g:绿色 b:蓝色 w:白色 c:青色 m:洋红 y:黄色 k:黑色  其他:#00ff00
        linestyle = '-'     '-':实线  '--':虚线  '-.':点划线  ':':点虚线  '':无线条
        linewidth = 5       线条粗细
        alpha = 0.5         透明度
        label = 'xxx'       图例名称
    """

    x_ticks = ["10点{}分".format(i) for i in x if i < 60]
    x_ticks += ["11点{}分".format(i - 60) for i in x if i > 60]

    font = font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc', size=20)
    plt.xticks(x[::5], x_ticks[::5], rotation=45, fontproperties=font)
    plt.xlabel("时间", fontproperties=font)

    plt.yticks(range(15, 40))
    plt.ylabel("温度℃", fontproperties=font)
    plt.title("10点到12点每分钟的温度变化情况", fontproperties=font)

    plt.legend(prop=font, loc='upper left')  # 显示图例 loc = '' 位置

    plt.show()


if __name__ == "__main__":
    main()
