# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/14
# @Desc  :

"""
greenlet已经实现了协程，但是这个还的人工切换，是不是觉得太麻烦了，不要捉急，
python还有一个比greenlet更强大的并且能够自动切换任务的模块gevent

其原理是当一个greenlet遇到IO(指的是input output 输入输出，比如网络、文件操作等)操作时，
比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。

由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，
就保证总有greenlet在运行，而不是等待IO
"""

import gevent, random, time
from gevent import monkey

# 将程序中用到的耗时操作的代码，换为gevent中自己实现的模块
monkey.patch_all()


def func(name, n):
    for i in range(n):
        print("%s --> %d" % (name, i))
        time.sleep(random.random())


def main():
    g1 = gevent.spawn(func, "g111", 10)
    g2 = gevent.spawn(func, "g222", 10)
    g3 = gevent.spawn(func, "g333", 10)
    g4 = gevent.spawn(func, "g444", 10)

    gevent.joinall([g1, g2, g3, g4])


if __name__ == "__main__":
    main()
