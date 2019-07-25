# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/7/24
# @Desc  : 
"""
代理（proxies参数）
    如果需要使用代理，你可以通过为任意请求方法提供 proxies 参数来配置单个请求

    1.准备一堆的ip地址，组成ip池，随机选择一个ip来用
        记录ip的使用次数，随机规则优先使用次数少的ip
    2.检查代理可用性
        添加超时参数，判断代理的质量
        代理ip质量检查的网站

    https://proxy.mimvp.com/freesecret.php
"""

import requests


def main():
    # 根据协议类型，选择不同的代理
    proxies = {
        "http": "http://42.3.23.231:30454",
        "https": "http://12.34.56.79:9527",
    }

    # 如果代理需要使用HTTP Basic Auth，可以使用下面这种格式： 账号:密码@ip:port
    proxy = {"http": "mr_mao_hacker:sffqry9r@61.158.163.130:16816"}

    response = requests.get("http://www.baidu.com", proxies=proxies)
    print(response.text)


if __name__ == "__main__":
    main()
