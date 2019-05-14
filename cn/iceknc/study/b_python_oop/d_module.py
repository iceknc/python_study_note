"""
模块
    import 模块名
        通过 模块名. 使用模块提供的工具 -- 全局变量、函数、类
    import 模块名 as 别名  别名应该使用大驼峰命名规则

    from 模块名 import 工具名
        从某一个模块中，导入部分工具
        导入之后，不需要通过 模块名.  就可以直接使用工具

    如果两个模块，存在同名的函数，那么后导入模块的函数，会覆盖掉先导入的函数

    from 模块名 import *
        从某一个模块中，导入全部工具
        导入之后，不需要通过 模块名.  就可以直接使用工具

    导入模块时，会先搜索当前模块指定模块名的文件，如果有救直接导入，没有再搜索系统目录
    __file__可以查看模块的完整路径

    在导入文件时，文件中所有没有任何缩进的代码都会被执行一遍

    __name__
        Python的一个内置属性
        如果是被其他文件导入的，__name__ 就是模块名
        如果是当前执行的程序， __name__ 是 __main__
"""

import cn.iceknc.study.b_python_oop.a_oop as OOP

print(OOP.__file__)

def test():
    cat = OOP.Cat("Jerry")
    cat.sleep()

if __name__ == "__main__":
    test()
