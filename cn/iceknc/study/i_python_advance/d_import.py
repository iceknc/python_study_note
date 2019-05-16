# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/16
# @Desc  : 
"""
路径搜索
    从上面列出的目录里依次查找要导入的模块文件
    '' 表示当前路径
    列表中的路径的先后顺序代表了python解释器在搜索模块时的先后顺序

重新导入模块
    模块被导入后，import module不能重新导入模块，重新导入需用reload
    from aa import *  reload 无效

"""
import sys
import importlib




def main():
    print(sys.path)

    sys.path.append("a/b/c/d")
    print(sys.path)

    sys.path.insert(0, "a/b/c/d")
    print(sys.path)

    importlib.reload(sys)

if __name__ == "__main__":
    main()
