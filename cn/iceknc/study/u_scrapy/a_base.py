# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/6
# @Desc  : 
"""
Scrapy 框架
    Scrapy 是用纯python实现一个为了爬取网站数据，提取结构性数据而编写的应用框架。

    架构
                               ----->  Scheduler -------------------- Requests ------------|      Internet
                               |           |                                               |           |
                               |           |                                               |           |
                               |           |                                               |           |
                            Requests       |                                               |           |
                               |           |                                               v           |
    Item Pipeline ------------------- Scrapy Engine ----- Downloader Middlewares ----- Downloader -----|
        ^                      |           |                                               |
        |                      |           |                                               |
        |                      |           |                                               |
        |                      |      Spider Middlewares                                Responses
        |                      |           |                                               |
        |                      |           |                                               |
        |                      |           |                                               |
        |                      |-------- Spider -------------------------------------------|
        |                                  |
        |----- Items ----------------------|

    Scrapy Engine(引擎):负责Spider、Item Pipeline、Downloader、Scheduler中间的通讯，信号、数据传递等
    Scheduler(调度器):  负责接收引擎发送过来的Request请求，并按照一定的方式进行整理排列，入队，当引擎需要时，交还给引擎
    Downloader(下载器): 负责下载引擎发送的所有Request请求，并将其获取到的Response交还给引擎，由引擎交给Spider处理
    Spider(爬虫) :      负责处理所有Responses，分析提取数据，获取item字段需要的数据，并将需要跟进的url提取交给引擎，再次进入调度器
    Item Pipeline(管道):负责处理爬虫中获取到的item，并进行后期处理（详细分析，过滤，存储等）
    Downloader Middlewares(下载中间件): 一个可以自定义扩展下载功能的组件
    Spider Middlewares(Spider中间件): 一个可以自定义扩展和操作引擎和爬虫中间通信的功能组件（比如进入爬虫的Response和从爬虫出去的Request）

制作Scrapy 爬虫一共需要4步
    1.新建项目 scrapy startproject xxx
    2.明确目标 编写item.py
    3.制作爬虫 spider/xxspider.py
    4.存储内容 piplines.py
"""

def main():
    pass


if __name__ == "__main__":
    main()
    






