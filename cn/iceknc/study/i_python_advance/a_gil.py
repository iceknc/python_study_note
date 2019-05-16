# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/16
# @Desc  : 

"""
GIL（全局解释器锁）
    GIL面试题如下
        描述Python GIL的概念， 以及它对python多线程的影响？编写一个多线程抓取网页的程序，
        并阐明多线程抓取程序是否可比单线程性能有提升，并解释原因。

    参考答案:
        Python语言和GIL没有半毛钱关系。仅仅是由于历史原因在Cpython虚拟机(解释器)，难以移除GIL。
        GIL：全局解释器锁。每个线程在执行的过程都需要先获取GIL，保证同一时刻只有一个线程可以执行代码。
        线程释放GIL锁的情况： 在IO操作等可能会引起阻塞的system call之前,可以暂时释放GIL,但在执行完毕后,
        必须重新获取GIL Python 3.x使用计时器（执行时间达到阈值后，当前线程释放GIL）或Python 2.x，tickets计数达到100
        Python使用多进程是可以利用多核的CPU资源的。
        多线程爬取比单线程性能有提升，因为遇到IO阻塞会自动释放GIL锁
"""

def main():
    pass


if __name__ == "__main__":
    main()
    






