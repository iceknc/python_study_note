"""
python 中，所有 非数字型变量 都支持以下特点：
    都是一个序列 sequence，也可以理解为容器
    取值 []
    遍历 for in
    计算长度、最大/最小值、比较、删除
    链接 + 和重复 *
    切片

列表用 [] 定义，数据之间使用 , 分割

list[] 从列表中取值
list.index(data) 获取数据第一次出现的索引
del list[] 删除指定索引
list.remove(data) 删除第一个出现的指定数据
len(list) 获取列表长度
list.count(data) 数据在列表中出现的次数
list.sort() 升序排列
list.sort(reverse=True) 降序排列
list.reverse() 反序
list.pop() 删除末尾数据
list.pop(index) 删除指定索引的数据
list.insert(index, data) 指定索引插入数据
list.append(data) 末尾追加数据
list.extend(list_data) 末尾追加一个列表数据
list.clear() 清空数据
"""

name_list = ["zhangsan", "lisi", "wangwumazi"]

i = 0
while i < len(name_list):
    print(name_list[i])
    i += 1

for item in name_list:
    print(item)

print(name_list.count("zhangsan"))

name_list.sort()
print(name_list)

name_list.sort(reverse=True)
print(name_list)

name_list.reverse()
print(name_list)
