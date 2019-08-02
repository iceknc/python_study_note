# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/2
# @Desc  : 
"""
mongoDB 基础命令
    db                  查看当前的数据库
    show dbs/databases  查看所有的数据库
    use db_name         查看所有的数据库
    db.dropDatabase()   删除当前的数据库

集合 可以认为是表
    不手动创建集合：
        向不存在的集合中第一次加入数据时，集合会被创建出来
    手动创建集合：
        db.createCollection(name, options)
        db.createCollection("example")
        db.createCollection("example",{capped:true, size:10})
            capped：默认值为false，表示不设置上限， 为true时表示设置上限
            size：当capped值为true时，需要指定这个参数，表示上限大小，当文档达到这个上限时，之前的值会被覆盖，单位为字节
    查看集合：show collections
    删除集合：db.集合名称.drop()

数据类型
    Object ID： 文档ID
        每个文档都有一个属性， 为_id， 保证每个文档的唯一性
        可以自己去设置_id插入文档，如果没有提供， 那么MongoDB为每个文档提供了⼀个独特的_id， 类型为objectID
        objectID是一个12字节的十六进制数：
            前4个字节为当前时间戳
            接下来3个字节的机器ID
            接下来的2个字节中MongoDB的服务进程id
            最后3个字节是简单的增量值

    String：    字符串， 最常用， 必须是有效的UTF-8
    Boolean：   存储一个布尔值， true或false
    Integer：   整数可以是32位或64位， 这取决于服务器
    Double：    存储浮点值
    Arrays：    数组或列表， 多个值存储到一个键
    Object：    用于嵌入式的文档， 即一个值为一个文档
    Null：      存储Null值
    Timestamp： 时间戳， 表示从1970-1-1到现在的总秒数
    Date：      存储当前日期或时间的UNIX时间格式
        创建日期语句如下 ：参数的格式为YYYY-MM-DD
            new Date('2017-12-20')

插入
    db.集合名称.insert(document)
    db.stu.insert({name:'gj',gender:1})
    db.stu.insert({_id:"20170101",name:'gj',gender:1})
    插入文档时， 如果不指定_id参数， MongoDB会为文档分配一个唯一的ObjectId

保存
    db.集合名称.save(document)
    如果文档的_id已经存在则修改， 如果文档的_id不存在则添加

简单查询
    db.集合名称.find()
        返回全部数据

更新
    db.集合名称.update(<query> ,<update>,{multi: <boolean>})
        参数query:查询条件
        参数update:更新操作符
        参数multi:可选， 默认是false，表示只更新找到的第一条记录， 值为true表示把满足条件的文档全部更新

    db.stu.update({name:'hr'},{name:'mnc'})           更新一条
    db.stu.update({name:'hr'},{$set:{name:'hys'}})    更新一条
    db.stu.update({},{$set:{gender:0}},{multi:true})  更新全部
        注意："multi update only works with $ operators"

删除
    db.集合名称.remove(<query>,{justOne: <boolean>})
        参数query:可选，删除的文档的条件
        参数justOne:可选，如果设为true或1，则只删除一条，默认false， 表示删除多条

"""

def main():
    pass


if __name__ == "__main__":
    main()
    






