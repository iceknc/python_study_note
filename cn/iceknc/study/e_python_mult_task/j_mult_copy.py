# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/14
# @Desc  : 
import os, multiprocessing


def main():
    # 1 获取文件夹的名字
    folder_name = "F://mp3"

    # 2 创建一个新的文件夹
    try:
        os.mkdir(folder_name + "[copy]")
    except Exception:
        pass

    # 3 获取文件夹中所有文件名字
    file_list = os.listdir(folder_name)

    # 4 创建进程池
    pool = multiprocessing.Pool(2)

    # 5 用queue统计进度
    queue = multiprocessing.Manager().Queue()

    total_size = 0
    # 6 向进程池中添加任务
    for item in file_list:
        total_size += os.path.getsize(folder_name + "/" + item)
        pool.apply_async(copy, args=(folder_name + "/" + item, folder_name + "[copy]/" + item, queue))

    pool.close()
    # pool.join()
    current_size = 0
    current_progress = 0
    while True:
        get = queue.get()
        current_size += get
        progress = round(current_size * 100 / total_size, 2)

        #控制进度大于0.01才打印
        if progress != current_progress:
            current_progress = progress
            print("progress -- %.02f%%" % current_progress)
        if current_size == total_size:
            break
    print("复制完成 =================")


def copy(from_dir, to_dir, queue):
    print("%d @ %s --> %s start" % (os.getpid(), from_dir, to_dir))
    f_from = open(from_dir, "rb")
    f_to = open(to_dir, "wb")

    while True:
        read = f_from.read(1024)
        queue.put(len(read))
        if read:
            f_to.write(read)
        else:
            break

    f_from.close()
    f_to.close()


def show_progress():
    pass


if __name__ == "__main__":
    main()
