# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/14
# @Desc  : 

"""
Queue
    实现多进程之间的数据传递

    初始化Queue()对象时（例如：q=Queue()），若括号中没有指定最大可接收的消息数量，
    或数量为负值，那么就代表可接受的消息数量没有上限（直到内存的尽头）

    Queue.qsize()：返回当前队列包含的消息数量

    Queue.empty()：如果队列为空，返回True，反之False

    Queue.full()：如果队列满了，返回True,反之False

    Queue.get([block[, timeout]])：获取队列中的一条消息，然后将其从列队中移除，block默认值为True；
        1）如果block使用默认值，且没有设置timeout（单位秒），消息列队如果为空，此时程序将被阻塞（停在读取状态），
        直到从消息列队读到消息为止，如果设置了timeout，则会等待timeout秒，若还没读取到任何消息，则抛出"Queue.Empty"异常；
        2）如果block值为False，消息列队如果为空，则会立刻抛出"Queue.Empty"异常；

    Queue.get_nowait()：相当Queue.get(False)；

    Queue.put(item,[block[, timeout]])：将item消息写入队列，block默认值为True；
        1）如果block使用默认值，且没有设置timeout（单位秒），消息列队如果已经没有空间可写入，此时程序将被阻塞（停在写入状态），
        直到从消息列队腾出空间为止，如果设置了timeout，则会等待timeout秒，若还没空间，则抛出"Queue.Full"异常；
        2）如果block值为False，消息列队如果没有空间可写入，则会立刻抛出"Queue.Full"异常；

    Queue.put_nowait(item)：相当Queue.put(item, False)；

"""

import multiprocessing
import time
import random


# 写数据进程执行的代码
def write(q):
    for value in ["A", "B", "C", "D", "E"]:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码
def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print('Get %s from queue.' % value)
            time.sleep(random.random())
        else:
            break


def main():
    q = multiprocessing.Queue()
    pw = multiprocessing.Process(target=write, args=(q,))
    pr = multiprocessing.Process(target=read, args=(q,))
    pw.start()
    # 等待pw结束
    # pw.join()
    pr.start()
    pr.join()
    print('所有数据都写入并且读完')


if __name__ == "__main__":
    main()
