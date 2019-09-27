# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/11
# @Desc  : 
"""
数据结构
    redis是key-value的数据结构，每条数据都是⼀个键值对
    键的类型是字符串    注意：键不能重复
    值的类型分为五种：
        字符串string
        哈希hash
        列表list
        集合set
        有序集合zset

键命令
    查找键，参数支持正则
        keys pattern
    判断键是否存在，存在返回1，不存在返回0
        exists key
    查看键对应的值类型
        type key
    删除键及对应的值
        del key1 key2
    设置过期时间，以秒为单位，如果没有指定过期时间则会一直存在
        expire key seconds
    查看有效时间，以秒为单位
        ttl key

string类型
    字符串类型是Redis中最为基础的数据存储类型，它在Redis中是二进制安全的，这便意味着该类型可以接受任何格式的数据，
    如JPEG图像数据或Json对象描述信息等。在Redis中字符串类型的Value最多可以容纳的数据长度是512M。
    设置键值
        set key value
    设置键值及过期时间，以秒为单位
        setex key seconds value
    设置多个键值
        mset key1 value1 key2 value2 ...
    追加值
        append key value
    获取：根据键获取值，如果不存在此键则返回nil
        get key
    根据多个键获取多个值
        mget key1 key2 ...
hash类型
    hash用于存储对象，对象的结构为属性、值，值的类型为string
    设置单个属性
        hset key field value
    设置多个属性
        hmset key field1 value1 field2 value2 ...
    获取指定键所有的属性
        hkeys key
    获取一个属性的值
        hget key field
    获取多个属性的值
        hmget key field1 field2 ...
    获取所有属性的值
        hvals key
    删除整个hash
        del key
    删除属性，属性对应的值会被一起删除
        hdel key filed1 field2 ...
list类型
    列表的元素类型为string  按照插⼊顺序排序
    在左侧插入数据
        lpush key value1 value2 ...
    在右侧插入数据
        rpush key value1 value2 ...
    在指定元素的前或后插入新元素
        linsert key before/after 现有元素 新元素
    返回列表里指定范围内的元素
        lrange key start stop
            start、stop为元素的下标索引
            索引从左侧开始，第一个元素为0
            索引可以是负数，表示从尾部开始计数，如-1表示最后一个元素
    设置指定索引位置的元素值
        lset key index value
            索引从左侧开始，第一个元素为0
            索引可以是负数，表示尾部开始计数，如-1表示最后一个元素
    删除指定元素
        lrem key count value
            将列表中前count次出现的值为value的元素移除
            count > 0: 从头往尾移除    count < 0: 从尾往头移除    count = 0: 移除所有
set类型
    无序集合    元素为string类型    元素具有唯一性，不重复
    说明：对于集合没有修改操作
    添加元素
        sadd key member1 member2 ...
    返回所有的元素
        smenbers key
    删除指定元素
        srem key
zset类型
    有序集合    元素为string类型    元素具有唯⼀性，不重复
    每个元素都会关联一个double类型的score，表示权重，通过权重将元素从小到大排序
    说明：没有修改操作
    添加元素
        zadd key score1 member1 score2 member2 ...
    获取元素
        zrange key start stop
            返回指定范围内的元素
            start、stop为元素的下标索引
            索引从左侧开始，第一个元素为0
            索引可以是负数，表示从尾部开始计数，如-1表示最后一个元素
    删除指定元素
        zrem key member1 member2 ...
"""

def main():
    pass


if __name__ == "__main__":
    main()
    






