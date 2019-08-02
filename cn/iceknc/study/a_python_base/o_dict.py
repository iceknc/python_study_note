"""
dictionary 字典
    列表是有序的对象集合
    字典是无序的对象集合
用{}定义
用键值对存储数据
    键 key 是索引
    值 value 是数据
    键和值之间使用 : 分隔  数据之间用 , 分隔
    键必须是唯一的
    值可以是任意数据

dict[key] 取值
dict[key] = data 增加/修改  存在key，则是修改，不存在就是新增元素
dict.pop(key) 删除数据
len(dict) 统计元素数量
dict.update(temp_dict) 合并字典 如果被合并的字典中包含已经存在的键，会覆盖原有的值
dict.clear() 清空字典
"""

dict = {"name": "zhangsan",
        "gender": True,
        "height": 1.75}

print(dict)
print(dict["name"])
dict["age"] = 18
print(dict)
dict["age"] = 21
print(dict)
dict.pop("age")
print(dict)

temp_dic = {"name": "lisi"}
dict.update(temp_dic)
print(dict)

for k in dict:
    print(k, end=" - ")
    print(dict[k])

count_dict = {
    'b': 2,
    'h': 2,
    'c': 5,
    'e': 4,
    'w': 3,
    'q': 3,
    'a': 7,
}
#按value从小到大排序
a = sorted(count_dict.items(), key=lambda x: x[1])
#按value从大到小排序
a1 = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
#按key从小到大排序
a2 = sorted(count_dict.items(), key=lambda x: x[0])
#按key从大到小排序
a3 = sorted(count_dict.items(), key=lambda x: x[0], reverse=True)
#切片取vlaue最大的3个
a4 = a1[:3]