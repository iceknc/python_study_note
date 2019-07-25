# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/7/24
# @Desc  : 
"""
Requests也可以为HTTPS请求验证SSL证书：
    要想检查某个主机的SSL证书，你可以使用 verify 参数（也可以不写）
"""
import requests


def main():
    response = requests.get("https://www.baidu.com/", verify=True)
    print(response.content.decode())

    response = requests.get("https://www.12306.cn/mormhweb/")
    print(response.content.decode())

if __name__ == "__main__":
    main()
