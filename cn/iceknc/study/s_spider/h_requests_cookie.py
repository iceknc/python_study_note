# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/7/24
# @Desc  :
"""
Cookies
    如果一个响应中包含了cookie，那么我们可以利用 cookies参数拿到
"""

import requests


def main():
    response = requests.get("https://www.baidu.com")

    cookie_jar = response.cookies

    dict = requests.utils.dict_from_cookiejar(cookie_jar)

    print(cookie_jar)
    print(dict)


if __name__ == "__main__":
    main()
