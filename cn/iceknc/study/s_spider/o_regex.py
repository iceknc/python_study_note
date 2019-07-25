# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/7/25
# @Desc  : 
"""
re 模块的一般使用步骤如下：
    使用 compile() 函数将正则表达式的字符串形式编译为一个 Pattern 对象
    通过 Pattern 对象提供的一系列方法对文本进行匹配查找，获得匹配结果，一个 Match 对象。
        match 方法：从起始位置开始查找，一次匹配
        search 方法：从任何位置开始查找，一次匹配
        findall 方法：全部匹配，返回列表
        finditer 方法：全部匹配，返回迭代器
        split 方法：分割字符串，返回列表
        sub 方法：替换
    最后使用 Match 对象提供的属性和方法获得信息，根据需要进行其他的操作

    re.DOTALL  re.S  .匹配包含\n
"""

import re


def main():
    print(re.findall(".", "\n"))
    print(re.findall(".", "\n", re.DOTALL))
    print(re.findall(".", "\n", re.S))


if __name__ == "__main__":
    main()
