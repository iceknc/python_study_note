# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/9
# @Desc  : 
"""
生成crawlspider
    scrapy genspider -t crawl <spider_name> <all_domain>

CrawlSpider中不能再有以parse为名字的数据提取方法，这个方法被CrawlSpider用来实现基础url提取等功能

一个Rule对象接收很多参数，首先第一个是包含url规则的LinkExtractor对象，常用的还有callback（制定满足规则的url的解析函数 字符串）和
follow（response中提取的链接是否需要跟进）

不指定callback函数的情况下，如果follow为True，满足该rule的url还会继续被请求

如果多个rule都满足某一个url，会从rules中选择第一个满足条件的进行操作

LinkExtractor更多常见参数：
    allow：满足括号中的正则表达式的URL会被提取，如果为空，则全部匹配
    deny：满足括号中的正则表达式的URL一定不提取，优先级高于allow
    allow_domains：会被提取的链接的domains
    deny_domains：一定不会被提取的链接的domains
    restrict_xpaths：使用xpath表达式，和allow共同作用过滤链接，即xpath满足范围内的url地址会被提取

spiders.Rule常见参数：
    link_extractor：是一个LinkExtractor对象，用于定义需要提取的链接
    callback：从link_extractor中没获取到链接时，参数所指定的值为回调函数
    follow：是一个布尔值，指定了根据该规则从Response提取的链接是否需要跟进，如果callback为None，follow默认设置为True，否则默认为False
    process_links：指定该spider中哪个的函数会被调用，从link_extractor中获取到链接列表时将会调用该函数，该方法主要用来过滤url
    process_request：指定该spider中哪个函数将会被调用，该规则提取到每个request时都会调用该函数，用来过滤Request

"""

def main():
    pass


if __name__ == "__main__":
    main()
    






