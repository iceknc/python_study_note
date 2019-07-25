# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/7/24
# @Desc  : 

import requests

def main():
    unquote = requests.utils.unquote("https://tieba.baidu.com/f?ie=utf-8&kw=%E6%9D%8E%E6%AF%85&fr=search")
    print(unquote)
    quote = requests.utils.quote(unquote)
    print(quote)


if __name__ == "__main__":
    main()
    






