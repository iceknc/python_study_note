# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/7/24
# @Desc  : 
import requests


def main():
    response = requests.get("http://www.baidu.com/img/superlogo_c4d7df0a003d3db9b65e9ef0fe6da1ec.png?where=super")
    with open("a.png", "wb") as f:
        f.write(response.content)


if __name__ == "__main__":
    main()
