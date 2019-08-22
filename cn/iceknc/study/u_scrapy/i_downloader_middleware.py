# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/12
# @Desc  : 
"""
Downloader Middleware
    下载中间件是处于引擎(crawler.engine)和下载器(crawler.engine.download())之间的一层组件，可以有多个下载中间件被加载运行。
    当引擎传递请求给下载器的过程中，下载中间件可以对请求进行处理 （例如增加http header信息，增加proxy信息等）；
    在下载器完成http请求，传递响应给引擎的过程中， 下载中间件可以对响应进行处理（例如进行gzip的解压等）
    要激活下载器中间件组件，将其加入到 DOWNLOADER_MIDDLEWARES 设置中。 该设置是一个字典(dict)，键为中间件类的路径，
    值为其中间件的顺序(order)。
        DOWNLOADER_MIDDLEWARES = {
            'mySpider.middlewares.MyDownloaderMiddleware': 543,
        }
    编写一个Downloader Middleware和我们编写一个pipeline一样，定义一个类，然后在setting中开启

    默认方法：
        process_request(self, request, spider):
            当每个request通过下载中间件时，该方法被调用。
            process_request() 必须返回以下其中之一：一个 None 、一个 Response 对象、一个 Request 对象或 raise IgnoreRequest:
                None: Scrapy将继续处理该request，执行其他的中间件的相应方法，直到合适的下载器处理函数
                (download handler)被调用， 该request被执行(其response被下载)。

                Response对象: Scrapy将不会调用 任何 其他的 process_request() 或 process_exception() 方法，或相应地下载函数；
                其将返回该response。 已安装的中间件的 process_response() 方法则会在每个response返回时被调用。

                Request对象: Scrapy则停止调用 process_request方法并重新调度返回的request。当新返回的request被执行后，相应的中间
                件链将会根据下载的response被调用。

                raise IgnoreRequest异常: 则安装的下载中间件的 process_exception() 方法会被调用。如果没有任何一个方法处理该异
                常，则request的errback(Request.errback)方法会被调用。如果没有代码处理抛出的异常，则该异常被忽略且不记录(不同
                于其他异常那样)。
        process_response(self, request, response, spider):
            当下载器完成http请求，传递响应给引擎的时候调用
            process_request() 必须返回以下其中之一: 返回一个 Response 对象、返回一个Request对象或raise一个IgnoreRequest异常。
                Response (可以与传入的response相同，也可以是全新的对象)， 该response会被在链中的其他中间件的
                process_response() 方法处理。

                Request对象：则中间件链停止， 返回的request会被重新调度下载。处理类似于 process_request() 返回request所做的那样。

                IgnoreRequest异常： 则调用request的errback(Request.errback)。 如果没有代码处理抛出的异常，则该异常被忽略且不
                记录(不同于其他异常那样)。



反反爬虫相关机制
    动态设置User-Agent（随机切换User-Agent，模拟不同用户的浏览器信息）
        class RandomUserAgent(object):
            process_request(self, request, spider):
                userAgent = random.choice(USER_AGENTS)
                request.headers['User-Agent'] = userAgent
    禁用Cookies（也就是不启用cookies middleware，不向Server发送cookies，有些网站通过cookie的使用发现爬虫行为）
        通过COOKIES_ENABLED 控制 CookiesMiddleware 开启或关闭
    设置延迟下载（防止访问过于频繁，设置为 2秒 或更高）
    Google Cache 和 Baidu Cache：如果可能的话，使用谷歌/百度等搜索引擎服务器页面缓存获取页面数据。
    使用IP地址池：VPN和代理IP，现在大部分网站都是根据IP来ban的。
        class RandomUserAgent(object):
            process_request(self, request, spider):
                request.meta['proxy'] = "http://0.0.0.0:000"
    使用 Crawlera（专用于爬虫的代理组件），正确配置和设置下载中间件后，项目所有的request都是通过crawlera发出。
        DOWNLOADER_MIDDLEWARES = {
            'scrapy_crawlera.CrawleraMiddleware': 600
        }
        CRAWLERA_ENABLED = True
        CRAWLERA_USER = '注册/购买的UserKey'
        CRAWLERA_PASS = '注册/购买的Password'

"""
from fake_useragent import UserAgent

def main():
    ua = UserAgent(cache=True)
    print(ua.random)


if __name__ == "__main__":
    main()
    






