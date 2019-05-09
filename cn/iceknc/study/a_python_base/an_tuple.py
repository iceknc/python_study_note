"""
tuple 元祖用 () 定义，元素之间用逗号隔开
tuple 元祖与列表类似，不同之处在于元祖的元素不能修改
元祖只有一个元素时，需要在元素后面添加逗号
tuple[index] 取值
len(tuple) 元素数量
tuple.index(data) 数据首次出现的索引
tuple.count(data) 数据出现的次数

list(tuple) tuple --> list
tuple(list) list --> tuple

应用场景：
    函数的参数和返回值，一个函数可以接受任意多个参数，返回任意多个数据
    格式字符串
    不可修改的数据列表


"""

tuple_a = ("zhangsan",)

tuple_b = ("zhangsan", 18, 1.75)

print(tuple_b[2])

for item in tuple_b:
    print(item)

print(type(tuple_b))
list_b = list(tuple_b)
print(type(list_b))
tuple_b = tuple(list_b)
print(type(tuple_b))