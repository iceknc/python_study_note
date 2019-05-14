"""
def func():
    pass

def func(var1, var2):
    pass

def func(var1, var2):
    return var1 + var2

形参：定义函数时，小括号中的参数
实参：调用函数时，小括号中的参数
"""


def sya_hello():
    print("hello python")


def say(msg):
    print("hello %s" % msg)


def print_line(char='*', times=20):
    print(char * times)


sya_hello()

say("world")

print_line()
print_line("&", 50)
