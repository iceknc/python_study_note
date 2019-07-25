# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/7/23
# @Desc  : 
"""
Requests: 让 HTTP 服务人类
    Requests 继承了urllib的所有特性。Requests支持HTTP连接保持和连接池，支持使用cookie保持会话，支持文件上传，
    支持自动确定响应内容的编码，支持国际化的 URL 和 POST 数据自动编码。

理解一下 BytesIO 和StringIO
    很多时候，数据读写不一定是文件，也可以在内存中读写。
    StringIO顾名思义就是在内存中读写str。
    BytesIO 就是在内存中读写bytes类型的二进制数据

"""
import requests
from io import BytesIO, StringIO
from PIL import  Image

def main():
    baidu = requests.get("http://www.baidu.com")
    print(baidu.content)

    kw = {'wd': '长城'}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    # params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
    response = requests.get("http://www.baidu.com/s?", params=kw, headers=headers)
    # 查看响应内容，response.text 返回的是Unicode格式的数据
    print(response.text)
    # 查看响应内容，response.content返回的字节流数据
    print(response.content)
    # 查看完整url地址
    print(response.url)
    # 查看响应头部字符编码
    print(response.encoding)
    # 查看响应码
    print(response.status_code)

    img_url = "http://imglf1.ph.126.net/pWRxzh6FRrG2qVL3JBvrDg==/6630172763234505196.png"
    response = requests.get(img_url)
    f = BytesIO(response.content)
    img = Image.open(f)
    print(img.size)

if __name__ == "__main__":
    main()
    






