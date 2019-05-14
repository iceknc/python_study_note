# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/14
# @Desc  :

"""
进程
    系统进行资源分配和调度的一个独立单位

    能够完成多任务，比如在一台电脑能够同时运行多个qq

    一个程序至少有一个进程,一个进程至少有一个线程

    进程在执行过程中拥有独立的内存单元，而多个线程共享内存，从而极大地提高了程序的运行效率
线程
    线程的划分尺度小于进程(资源比进程少)，使得多线程程序的并发性高

    线程是进程的一个实体,是CPU调度和分派的基本单位,它是比进程更小的能独立运行的基本单位.
    线程自己基本上不拥有系统资源,只拥有一点在运行中必不可少的资源(如程序计数器,一组寄存器和栈),
    但是它可与同属一个进程的其他的线程共享进程所拥有的全部资源

    能够完成多任务，比如一个qq中的多个聊天窗口

    线线程不能够独立执行，必须依存在进程中

线程和进程在使用上各有优缺点：
    线程执行开销小，但不利于资源的管理和保护；而进程正相反。
"""

import multiprocessing
import time


def func_a():
    while True:
        print("a-----------a")
        time.sleep(1)


def func_b():
    while True:
        print("b-----------b")
        time.sleep(1)


def main():
    ta = multiprocessing.Process(target=func_a)
    tb = multiprocessing.Process(target=func_b)
    ta.start()
    tb.start()


if __name__ == "__main__":
    main()
