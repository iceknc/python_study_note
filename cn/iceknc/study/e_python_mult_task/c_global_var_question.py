"""
多线程-共享全局变量

假设两个线程t1和t2都要对全局变量g_num(默认是0)进行加1运算，t1和t2都各对g_num加10次，g_num的最终的结果应该为20。

但是由于是多线程同时操作，有可能出现下面情况：

    在g_num=0时，t1取得g_num=0。此时系统把t1调度为”sleeping”状态，把t2转换为”running”状态，t2也获得g_num=0
    然后t2对得到的值进行加1并赋给g_num，使得g_num=1
    然后系统又把t2调度为”sleeping”，把t1转为”running”。线程t1又把它之前得到的0加1后赋值给g_num。
    这样导致虽然t1和t2都对g_num加1，但结果仍然是g_num=1


如果多个线程同时对同一个全局变量操作，会出现资源竞争问题，从而数据结果会不正确
"""

import threading
import time

g_num = 0


def test1(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("test1  --> %d" % g_num)


def test2(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("test2  --> %d" % g_num)


def main():
    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))

    t1.start()
    t2.start()

    time.sleep(5)

    print("main  --> %d" % g_num)


if __name__ == '__main__':
    main()
