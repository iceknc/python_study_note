"""
并行：真的多任务
    cpu核数多于任务数
并发：假的多任务
    cpu核数小于任务数

主线程会等待所有的子线程结束后才结束
"""


import time
import threading


def sing():
    for i in range(10):
        print("sing ...")
        time.sleep(1)

    #如果创建Thread时执行的函数运行结束，那么意味着这个子线程结束了

def dance():
    for i in range(10):
        print("dance ...")
        time.sleep(1)

def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()

    while True:
        length = len(threading.enumerate())
        print('当前运行的线程数为：%d' % length)
        if length <= 1:
            break

        time.sleep(0.5)


if __name__ == '__main__':
    main()
