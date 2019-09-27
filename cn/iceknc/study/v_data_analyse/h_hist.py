# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/17
# @Desc  : 
from matplotlib import pyplot as plt
from matplotlib import font_manager


def main():
    a = [131, 98, 125, 131, 124, 139, 131, 117, 128, 108, 135, 138, 131, 102, 107, 114, 119, 128, 121, 142, 127, 130,
         124, 101, 110, 116, 117, 110, 128, 128, 115, 99, 136, 126, 134, 95, 138, 117, 111, 78, 132, 124, 113, 150,
         110, 117, 86, 95, 144, 105, 126, 130, 126, 130, 126, 116, 123, 106, 112, 138, 123, 86, 101, 99, 136, 123,
         117, 119, 105, 137, 123, 128, 125, 104, 109, 134, 125, 127, 105, 120, 107, 129, 116, 108, 132, 103, 136, 118,
         102, 120, 114, 105, 115, 132, 145, 119, 121, 112, 139, 125, 138, 109, 132, 134, 156, 106, 117, 127, 144, 139,
         139, 119, 140, 83, 110, 102, 123, 107, 143, 115, 136, 118, 139, 123, 112, 118, 125, 109, 119, 133, 112, 114,
         122, 109, 106, 123, 116, 131, 127, 115, 118, 112, 135, 115, 146, 137, 116, 103, 144, 83, 123, 111, 110, 111,
         100, 154, 136, 100, 118, 119, 133, 134, 106, 129, 126, 110, 111, 109, 141, 120, 117, 106, 149, 122, 122, 110,
         118, 127, 121, 114, 125, 126, 114, 140, 103, 130, 141, 117, 106, 114, 121, 114, 133, 137, 92, 121, 112, 146,
         97, 137, 105, 98, 117, 112, 81, 97, 139, 113, 134, 106, 144, 110, 137, 137, 111, 104, 117, 100, 111, 101,
         110, 105, 129, 137, 112, 120, 113, 133, 112, 83, 94, 146, 133, 101, 131, 116, 111, 84, 137, 115, 122, 106,
         144, 109, 123, 116, 111, 111, 133, 150]

    plt.figure(figsize=(15, 10), dpi=80)
    font = font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc', size=20)

    # 组数：将数据分组，当数据在100个以内时，按数据多少常分5~12组
    # 组距：每个小组的两个端点的距离
    # 组数 = 极差 / 组距 = (max(a) - min(a)) / bin_width
    bin_width = 3  # 设置组距为3
    num_bins = int((max(a) - min(a)) / bin_width)
    print(num_bins)

    # 传入需要统计的数据， 以及组数即可
    # plt.hist(a, num_bins)

    # 传入一个列表，长度为组数，值为分组依据，当组距不均匀的时候使用
    # plt.hist(a, [min(a) + i * bin_width for i in range(num_bins)])

    # density:bool 是否绘制频率分布直方图，默认为频数直方图
    plt.hist(a, num_bins, density=1)

    plt.xticks(list(range(min(a), max(a)))[::bin_width], rotation=45)
    plt.grid(True, linestyle='-.', alpha=0.5)
    plt.show()


if __name__ == "__main__":
    main()
