# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/7/24
# @Desc  :
"""
json string  -- json.loads() -->  python数据类型
json string  <-- json.dumps() --  python数据类型

包含json的类文件对象  -- json.load() -->  python数据类型
包含json的类文件对象  <-- json.dump() --  python数据类型

具有read() 或者write()方法的对象就是类文件对象
    f = open("a.txt","r")  f 以r打开，就会有read(), 就是一个类文件对象
"""
import json
from cn.iceknc.study.s_spider.m_retrying import parse_url
from pprint import pprint


def main():
    url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0"
    html_str = parse_url(url)
    ret = json.loads(html_str)
    pprint(ret)

    with open("douban.json", "w", encoding="utf-8") as  f:
        f.write(json.dumps(ret, ensure_ascii=False, indent=4))

    with open("douban1.json", "w", encoding="utf-8") as  f:
        json.dump(ret, f, ensure_ascii=False, indent=4)

    with open("douban.json", "r", encoding="utf-8") as  f:
        load = json.load(f)
        print(load)


if __name__ == "__main__":
    main()
