# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/14
# @Desc  : 

import time
from greenlet import greenlet


def task_a():
    while True:
        print("-----a-----")
        gr2.switch()
        time.sleep(0.1)


def task_b():
    while True:
        print("b----b----b")
        gr1.switch()
        time.sleep(0.1)


gr1 = greenlet(task_a)
gr2 = greenlet(task_b)


def main():
    gr1.switch()


if __name__ == "__main__":
    main()
