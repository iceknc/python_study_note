# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/11
# @Desc  : 
"""
安装Redis
    pip install redis
StrictRedis对象方法
    通过init创建对象，指定参数host、port与指定的服务器和端口连接，host默认为localhost，port默认为6379，db默认为0
        sr = StrictRedis(host='localhost', port=6379, db=0)  简写  sr=StrictRedis()
        对象方法参考a_base.py里的方法
"""
from redis import *


def main():
    sr = StrictRedis()
    sr.set('py_test_key', 'py_test_value')
    sr.hset('py_test_hash_name', 'py_test_hash_key', 'py_test_hash_value')
    print(sr.get('py_test_key'))
    print(sr.ttl('py_test_key'))
    print(sr.hkeys('py_test_hash_name'))
    print(sr.hget('py_test_hash_name', 'py_test_hash_key'))
    print(sr.hvals('py_test_hash_name'))


if __name__ == "__main__":
    main()
