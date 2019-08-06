# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/6
# @Desc  : 
"""
项目
    1.新建：scrapy startproject itcastSpider
        项目结构
            ----itcastSpider
                |----itcastSpider           项目的python模块
                |   |----__init__.py
                |   |----items.py        项目的目标文件库
                |   |----pipelines.py    项目的管道文件
                |   |----settings.py     项目的设置文件
                |   |----spiders         存储爬虫代码目录
                |       |----__init__.py
                |----scrapy.cfg           项目配置文件
    2.明确目标
        抓取 http://www.itcast.cn/channel/teacher.shtml 网站里所有讲师的姓名、授课分类、职称和个人信息
            打开itcastSpider目录下的items.py
            Item 定义结构化数据字段，用来保存爬取到的数据，有点像Python中的dict，但是提供了一些额外的保护减少错误。
            可以通过创建一个 scrapy.Item 类， 并且定义类型为 scrapy.Field的类属性来定义一个Item。
            接下来，创建一个ItcastItem 类，和构建item模型（model）。
    3.制作爬虫
        在当前目录下输入命令，将在mySpider/spider目录下创建一个名为itcast的爬虫，并指定爬取域的范围：
            scrapy genspider itcast "itcast.cn"

        其实也可以由我们自行创建itcast.py并编写上面的代码，只不过使用命令可以免去编写固定代码的麻烦
        要建立一个Spider， 你必须用scrapy.Spider类创建一个子类，并确定了三个强制的属性 和 一个方法。
            name = "" ：这个爬虫的识别名称，必须是唯一的，在不同的爬虫必须定义不同的名字。
            allow_domains = [] 是搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页，不存在的URL会被忽略。
            start_urls = () ：爬取的URL元祖/列表。爬虫从这里开始抓取数据，所以，第一次下载的数据将会从这些urls开始。
                              其他子URL将会从这些起始URL中继承性生成。

            parse(self, response) ：解析的方法，每个初始URL完成下载后将被调用，调用的时候传入从每一个URL传回的Response对象来作为唯一参数，
                                    主要作用如下：
                负责解析返回的网页数据(response.body)，提取结构化数据(生成item)
                生成需要下一页的URL请求。
    4.保存数据
        # json格式，默认为Unicode编码
        scrapy crawl itcast -o teachers.json

        # json lines格式，默认为Unicode编码
        scrapy crawl itcast -o teachers.jsonl

        # csv 逗号表达式，可用Excel打开
        scrapy crawl itcast -o teachers.csv

        # xml格式
        scrapy crawl itcast -o teachers.xml
"""

def main():
    pass


if __name__ == "__main__":
    main()
    






