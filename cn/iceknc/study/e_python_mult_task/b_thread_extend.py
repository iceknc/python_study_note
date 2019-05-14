"""
继承Thread类完成创建线程
"""

import threading
import time


class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.name = "MyThread"

    def run(self):
        for i in range(10):
            str = "My name is "+ self.name
            print(str)
            time.sleep(1)


if __name__ == '__main__':
    t = MyThread()
    t.start()
