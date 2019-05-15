# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/14
# @Desc  : 

"""
匹配开头结尾
    ^ 	匹配字符串开头
    $ 	匹配字符串结尾
"""

import re


def main():
    email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com", "xiaoWang@126.com"]

    for email in email_list:
        ret = re.match("[\w]{4,20}@163\.com", email)
        if ret:
            print("%s 是符合规定的邮件地址,匹配后的结果是:%s" % (email, ret.group()))
        else:
            print("%s 不符合要求" % email)

    for email in email_list:

        # 如果在正则表达式中需要用到某些普通的字符 比如 . 比如 ？, 仅仅需要在他们面前加上一个反斜杠
        ret = re.match("^[\w]{4,20}@(163|126)\.com$", email)
        if ret:
            print("%s 是符合规定的邮件地址,匹配后的结果是:%s" % (email, ret.group()))
        else:
            print("%s 不符合要求" % email)


if __name__ == "__main__":
    main()
