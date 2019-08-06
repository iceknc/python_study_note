# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/6
# @Desc  : 
"""
索引
    提升查询速度

    测试: 插入10万条数据到数据库中
        for(i=0;i<100000;i++){db.test.insert({name:"test_"+i,age:i})}
        db.test.find({name:"test_88888"}).explain("executionStats")

        建立索引
        db.test.ensureIndex({name:1})  1表示升序,-1表示降序

        db.test.find({name:"test_88888"}).explain("executionStats")

    在默认情况下创建的索引均不是唯一索引

    创建唯一索引
        db.test.ensureIndex({"name":1},{"unique",true})
    创建唯一索引并消除重复
        db.test.ensureIndex({"name":1},{"unique",true, "dropDups", true})
    建立联合索引
        db.test.ensureIndex({name:1, age:1})
    查看当前集合的所有索引
        db.test.getIndexes()
    删除索引
        db.test.dropIndex("索引名称")
"""

def main():
    pass


if __name__ == "__main__":
    main()
    






