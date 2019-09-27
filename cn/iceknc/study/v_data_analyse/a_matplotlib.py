# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/12
# @Desc  : 
from matplotlib import pyplot as plt

def main():
    plt.figure(figsize=(20,8),dpi=50) #在图像模糊的时候可以传入dpi，让图像更加清晰
    x = range(2,26,2) #数据在x轴的位置，是一个可迭代对象
    y = [15,13,14.5,17,20,25,26,26,24,22,18,15] #数据在y轴的位置，是一个可迭代对象
    plt.plot(x,y)

    plt.xticks(x) #设置x轴刻度
    plt.xticks(x[::1]) #刻度太密集的时候，可以尝试切片

    plt.yticks(range(min(y), max(y)+1))#设置y轴刻度

    plt.savefig("./sig_size.png")
    plt.show()


if __name__ == "__main__":
    main()
    






