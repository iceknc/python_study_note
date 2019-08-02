# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/7/31
# @Desc  : 
"""
文件/目录的管理操作
    使用 os 模块

    文件操作
        rename(源文件名, 目标文件名|)
        remove(文件名)

    目录操作
        listdir 目录列表
        mkdir 创建目录
        rmdir 删除目录
        getcwd 获取当前目录
        chdir 修改工作目录
        path.isdir 判断是否是文件

    目录操作
        os.path.abspath(path)	返回绝对路径
        os.path.basename(path)	返回文件名
        os.path.commonprefix(list)	返回list(多个路径)中，所有path共有的最长的路径
        os.path.dirname(path)	返回文件路径
        os.path.exists(path)	如果路径 path 存在，返回 True；如果路径 path 不存在，返回 False。
        os.path.lexists	路径存在则返回True,路径损坏也返回True
        os.path.expanduser(path)	把path中包含的"~"和"~user"转换成用户目录
        os.path.expandvars(path)	根据环境变量的值替换path中包含的"$name"和"${name}"
        os.path.getatime(path)	返回最近访问时间（浮点型秒数）
        os.path.getmtime(path)	返回最近文件修改时间
        os.path.getctime(path)	返回文件 path 创建时间
        os.path.getsize(path)	返回文件大小，如果文件不存在就返回错误
        os.path.isabs(path)	判断是否为绝对路径
        os.path.isfile(path)	判断路径是否为文件
        os.path.isdir(path)	判断路径是否为目录
        os.path.islink(path)	判断路径是否为链接
        os.path.ismount(path)	判断路径是否为挂载点
        os.path.join(path1[, path2[, ...]])	把目录和文件名合成一个路径
        os.path.normcase(path)	转换path的大小写和斜杠
        os.path.normpath(path)	规范path字符串形式
        os.path.realpath(path)	返回path的真实路径
        os.path.relpath(path[, start])	从start开始计算相对路径
        os.path.samefile(path1, path2)	判断目录或文件是否相同
        os.path.sameopenfile(fp1, fp2)	判断fp1和fp2是否指向同一文件
        os.path.samestat(stat1, stat2)	判断stat tuple stat1和stat2是否指向同一个文件
        os.path.split(path)	把路径分割成 dirname 和 basename，返回一个元组
        os.path.splitdrive(path)	一般用在 windows 下，返回驱动器名和路径组成的元组
        os.path.splitext(path)	分割路径，返回路径名和文件扩展名的元组
        os.path.splitunc(path)	把路径分割为加载点与文件
        os.path.walk(path, visit, arg)	遍历path，进入每个目录都调用visit函数，visit函数必须有3个参数(arg, dirname, names)，
            dirname表示当前目录的目录名，names代表当前目录下的所有文件名，args则为walk的第三个参数
        os.path.supports_unicode_filenames	设置是否支持unicode路径名
"""

import os


def main():
    root_dir = "F://迅雷下载/good_gif/"
    files = all_path(root_dir)
    to_dir = "F://迅雷下载/good_gif_total/"
    if not os.path.exists(to_dir):
        os.mkdir(to_dir)

    count = 0
    for file in files:
        with open(os.path.abspath(file), "rb") as from_file:
            read = from_file.read()
            to_file_name = to_dir + str(count + 10000) + ".gif"
            with open(to_file_name, "wb") as to_file:
                print(to_file_name)
                to_file.write(read)
        count += 1


def all_path(dirname):
    result = []  # 所有的文件
    for main_dir, sub_dir, sub_file in os.walk(dirname):
        print("1:", main_dir)  # 当前主目录
        print("2:", sub_dir)  # 当前主目录下的所有目录
        print("3:", sub_file)  # 当前主目录下的所有文件

        for filename in sub_file:
            path = os.path.join(main_dir, filename)  # 合并成一个完整路径
            result.append(path)
    return result


if __name__ == "__main__":
    main()
