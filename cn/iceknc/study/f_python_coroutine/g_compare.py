# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/14
# @Desc  :

"""

进程、线程、协程对比
    理解如下的通俗描述

    有一个老板想要开个工厂进行生产某件商品（例如剪子）他需要花一些财力物力制作一条生产线，
    这个生产线上有很多的器件以及材料这些所有的 为了能够生产剪子而准备的资源称之为：进程

    只有生产线是不能够进行生产的，所以老板的找个工人来进行生产，这个工人能够利用这些材料
    最终一步步的将剪子做出来，这个来做事情的工人称之为：线程

    这个老板为了提高生产率，想到3种办法：
        在这条生产线上多招些工人，一起来做剪子，这样效率是成倍増长，即单进程 多线程方式

        老板发现这条生产线上的工人不是越多越好，因为一条生产线的资源以及材料毕竟有限，
        所以老板又花了些财力物力购置了另外一条生产线，然后再招些工人这样效率又再一步提高了，
        即多进程 多线程方式

        老板发现，现在已经有了很多条生产线，并且每条生产线上已经有很多工人了（即程序是多进程的，
        每个进程中又有多个线程），为了再次提高效率，老板想了个损招，规定：如果某个员工在上班时临
        时没事或者再等待某些条件（比如等待另一个工人生产完谋道工序 之后他才能再次工作） ，那么这个
        员工就利用这个时间去做其它的事情，那么也就是说：如果一个线程等待某些条件，可以充分利用这个时
        间去做其它事情，其实这就是：协程方式

简单总结

    进程是资源分配的单位
    线程是操作系统调度的单位
    进程切换需要的资源很最大，效率很低
    线程切换需要的资源一般，效率一般（当然了在不考虑GIL的情况下）
    协程切换任务资源很小，效率高
    多进程、多线程根据cpu核数不一样可能是并行的，但是协程是在一个线程中 所以是并发


"""


def main():
    pass


if __name__ == "__main__":
    main()
    





