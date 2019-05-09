"""
id(var) 获取变量的内存地址

python中
    变量和数据是分开存储的
    数据保存在内存中的一个位置
    变量中保存着数据在内存中的地址
    变量中记录数据的地址，就叫做引用

    如果变量已经被定义，当给一个变量赋值的时候，本质上修改了数据的引用

不可变类型 内存中的数据不允许被修改
    数字类型 int bool float complex long(2.x)
    字符串 string
    元组 tuple
可变类型
    列表 list
    字典 dict

字典的key只能使用不可变类型的数据


局部变量和全局变量
    函数内部定义的变量称为局部变量，只能在函数内部使用
    函数外部定义的变量称为全局变量，所有函数内部都可以使用这个变量
    不允许在函数内部修改全局变量，如果使用赋值语句，会生成一个跟全局变量同名的局部变量
    如果非改不可 加上global关键字
    全局变量要定义在所有函数的上方
    建议全局变量加上前缀 g_ 或者 gl_
"""


def test(num):
    print("函数内的参数地址 %d" % id(num))
    result = "result"
    print("函数返回值地址 %d" % id(result))
    return result

number = 123
print("准备传给函数的变量地址 %d" % id(number))
result = test(number)
print("接受到的函数返回值地址 %d" % id(result))

num = 10
def modify():
    global num
    num = 99
modify()
print(num)