"""
多线程-共享全局变量
"""

import threading
import time

g_num = 100
g_list = [1, 3]


# temp_list 和 g_list是同一个引用
def test1(temp_num, temp_list):
    global g_num
    g_num += 1
    g_list.append(5)

    temp_num += 1
    temp_list.append(7)
    print("test1  --> %d && %s" % (g_num, str(g_list)))


def test2():
    print("test2  --> %d && %s" % (g_num, str(g_list)))


def main():
    t1 = threading.Thread(target=test1, args=(g_num, g_list))
    t2 = threading.Thread(target=test2)

    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)

    print("main  --> %d && %s" % (g_num, str(g_list)))


if __name__ == '__main__':
    main()
