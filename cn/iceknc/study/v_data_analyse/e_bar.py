# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/16
# @Desc  : 
from matplotlib import pyplot as plt
from matplotlib import font_manager


def main():
    x = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇", "变形金刚5：最后的骑士", "摔跤吧！爸爸", "加勒比海盗5：死无对证",
         "金刚：骷髅岛", "极限特工：终极回归", "生化危机6：终章", "乘风破浪", "神偷奶爸3", "智取威虎山", "大闹天竺",
         "金刚狼3：殊死一战", "蜘蛛侠：英雄归来", "悟空传", "银河护卫队2", "情圣", "新木乃伊", ]

    y = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28, 11.12, 10.49, 10.3, 8.75, 7.55, 7.32, 6.99, 6.88,
         6.86, 6.58, 6.23]

    plt.figure(figsize=(30, 20), dpi=40)
    font = font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc', size=20)

    plt.bar(x, y, width=0.6, color='orange')

    x_label = ["{}".format(i) for i in x]
    plt.xticks(x, x_label, fontproperties=font, rotation=90)
    # plt.legend(prop=font, loc='upper right')  # 显示图例 loc = '' 位置

    plt.show()


if __name__ == "__main__":
    main()
