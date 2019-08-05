# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/5
# @Desc  : 
"""
备份
    mongodump -h dbhost -d dbname -o dbdirectory
        -h 服务器地址， 也可以指定端口号
        -d 需要备份的数据库名称
        -o 备份的数据库存放地址

    mongodump -h 192.168.196.128:27017 -d test1 -o ~/Desktop/test1bak


恢复
    mongorestore -h dbhost -d dbname --dir dbdirectory
        -h 服务器地址， 也可以指定端口号
        -d 需要备份的数据库名称
        -dir 备份数据所在位置
    mongorestore -h 192.168.196.128:27017 -d test2 --dir ~/Desktop/test1bak/test1
"""

def main():
    pass


if __name__ == "__main__":
    main()
    






