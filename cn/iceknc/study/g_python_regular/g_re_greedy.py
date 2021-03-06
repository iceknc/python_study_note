# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/15
# @Desc  :

"""
贪婪和非贪婪
    Python里数量词默认是贪婪的（在少数语言里也可能是默认非贪婪），总是尝试匹配尽可能多的字符；

    非贪婪则相反，总是尝试匹配尽可能少的字符。

    在"*","?","+","{m,n}"后面加上？，使贪婪变成非贪婪。
"""

import re


def main():
    s = "This is a number 234-235-22-423"
    r = re.match(".+(\d+-\d+-\d+-\d+)", s)
    print(r.group(1))  # 4-235-22-423

    r = re.match(".+?(\d+-\d+-\d+-\d+)", s)
    print(r.group(1))  # 234-235-22-423

    # 正则表达式模式中使用到通配字，那它在从左到右的顺序求值时，会尽量“抓取”满足匹配最长字符串，
    # 在我们上面的例子里面，“.+”会从字符串的启始处抓取满足模式的最长字符，其中包括我们想得到的
    # 第一个整型字段的中的大部分，“\d+”只需一位字符就可以匹配，所以它匹配了数字“4”，而“.+”则匹配
    # 了从字符串起始到这个第一位数字4之前的所有字符。
    # 解决方式：非贪婪操作符“？”，这个操作符可以用在"*","+","?"的后面，要求正则匹配的越少越好。


if __name__ == "__main__":
    main()
