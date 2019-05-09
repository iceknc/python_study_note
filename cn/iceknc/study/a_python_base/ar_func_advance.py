"""
函数返回值
    return 关键字
    返回多个数据，可以使用元组，小括号可以省略
    可以使用多个变量，一次接受函数的返回结果，变量的个数应该和元组中的元素个数保持一致

交换两个数字
    1：使用临时变量
        c = b
        b = a
        a = c
    2：不使用临时变量
        a = a + b
        b = a - b
        a = a - b
    3: python 专属
        a, b = b, a

函数内部针对参数赋值不会影响外部实参，无论是可变还是不可变类型的参数
但是使用方法修改可变参数，会影响外部实参

列表变量使用 += 本质上是调用了列表了extend() 方法

缺省参数
    定义函数时，可以给某个参数指定一个默认值，具有默认值的参数就叫缺省参数
    调用函数时，如果没有传入缺省参数的值，则在函数内部使用定义函数时指定的参数默认值
    函数的缺省参数，将常见的值设置为参数的缺省值，从而简化函数的调用
    缺省参数必须在参数列表的末尾

多值参数
    1. 参数名前面增加一个 * ，可以接收元组  *args
    2. 参数名前面增加两个 * ，可以接收字典  **kwargs
拆包
    调用多值参数时，如果希望将一个元组变量，直接传递给 args， 调用的时候，变量前加 *
    调用多值参数时，如果希望将一个字典变量，直接传递给 kwargs， 调用的时候，变量前加 **

递归
    一个函数内部调用函数自己
    必须要有出口
"""


def measure():
    temp = 39
    wetness = 89
    return temp, wetness


result_temp, result_wetness = measure()
print(result_temp)
print(result_wetness)

a = 1
b = 3

a, b = b, a
print(a)
print(b)


def var(num, list):
    """
    函数内部针对参数赋值不会影响外部实参，无论是可变还是不可变类型的参数
    :param num:
    :param list:
    :return:
    """
    print("来到了函数内部")
    num = 200
    list = [1, 2, 3]
    print(num)
    print(list)
    print("函数执行完成")


def varModify(num, list):
    """
    使用方法修改可变参数，会影响外部实参，不可变参数则没有影响
    :param num:
    :param list:
    :return:
    """
    print("来到了修改参数函数内部")
    num += 200
    list.extend([7, 8, 9])
    print(num)
    print(list)
    print("函数执行完成")


gl_num = 1
gl_list = [4, 5, 6]
var(gl_num, gl_list)
print(gl_num)
print(gl_list)
print("=" * 20)
varModify(gl_num, gl_list)
print(gl_num)
print(gl_list)


# 多值参数
def varMul(var, *args, **kwargs):
    print(var)
    print(args)
    print(kwargs)


varMul(1, 2, 3, 4, 5, name="lisi", age=18, gender=True)

args = (2, 3, 4, 5)
kwargs = {"a": 1, "b": 2}

varMul(123, args, kwargs)
varMul(123, *args, **kwargs)
