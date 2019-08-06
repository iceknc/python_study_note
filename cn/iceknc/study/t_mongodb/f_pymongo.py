# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/6
# @Desc  : 
from pymongo import MongoClient


def main():
    # 实例化连接
    client = MongoClient(host="localhost", port=27017)
    names = client.list_database_names()
    print(names)

    # 选择数据库
    db = client["pymongo_db"]
    collection_names = db.list_collection_names()
    print(collection_names)

    # 选择数据的集合
    collection = db["pymongo_collection"]

    # 更新数据
    collection.update_one({"name": "laowang"}, {"$set": {"age": 88}})

    # 更新一片数据
    collection.update_many({"name": "laowang"}, {"$set": {"age": 98}})

    # 查看全部
    find = collection.find()
    # for item in find:
    #     print(item)

    # 查看满足条件
    find = collection.find({"name": "laowang"})
    for item in find:
        print(item)
    one = collection.find_one({"name": "laowang"})
    # print(one)

    # 插入一条数据
    insert = collection.insert_one({"name": "laowang", "age": 18})
    print(insert)

    # 插入一片数据
    # item_list = [{"name": "name_{}".format(i)} for i in range(100)]
    # many = collection.insert_many(item_list)
    # for id in many.inserted_ids:
    #     print(id)

    # 删除一条数据
    delete_one = collection.delete_one({"name": "laowang"})
    print(delete_one)

    # 删除一片数据
    many = collection.delete_many({"name": "laowang"})
    print(many.deleted_count)


if __name__ == "__main__":
    main()
