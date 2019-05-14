"""
线程同步

# 创建锁
mutex = threading.Lock()

# 锁定
mutex.acquire()

# 释放
mutex.release()


如果这个锁之前是没有上锁的，那么acquire不会堵塞
如果在调用acquire对这个锁上锁之前 它已经被 其他线程上了锁，那么此时acquire会堵塞，直到这个锁被解锁为止

"""

import threading
import time

g_num = 0

mutex = threading.Lock()

def test1(num):
    global g_num
    for i in range(num):
        mutex.acquire()  # 上锁
        g_num += 1
        mutex.release()  # 释放
    print("test1  --> %d" % g_num)


def test2(num):
    global g_num
    for i in range(num):
        mutex.acquire()  # 上锁
        g_num += 1
        mutex.release()  # 释放
    print("test2  --> %d" % g_num)

def main():
    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))

    t1.start()
    t2.start()

    # 等待计算完成
    while len(threading.enumerate()) != 1:
        time.sleep(1)

    print("2个线程对同一个全局变量操作之后的最终结果是:%s" % g_num)


if __name__ == '__main__':
    main()