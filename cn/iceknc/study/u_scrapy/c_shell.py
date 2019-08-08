# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/7
# @Desc  : 
"""
Scrapy Shell
    Scrapy终端是一个交互终端，我们可以在未启动spider的情况下尝试及调试代码，也可以用来测试XPath或CSS表达式，
    查看他们的工作方式，方便我们爬取的网页中提取的数据。

    启动Scrapy Shell
        进入项目的根目录
            scrapy shell "http://...."

    Scrapy Shell根据下载的页面会自动创建一些方便使用的对象，例如 Response 对象，以及 Selector 对象 (对HTML及XML内容)。
        当shell载入后，将得到一个包含response数据的本地 response 变量，输入 response.body将输出response的包体，
        输出 response.headers 可以看到response的包头。

        输入 response.selector 时， 将获取到一个response 初始化的类 Selector 的对象，此时可以通过使用
        response.selector.xpath()或response.selector.css() 来对 response 进行查询。

        Scrapy也提供了一些快捷方式, 例如 response.xpath()或response.css()同样可以生效（如之前的案例）。

"""

def main():
    pass


if __name__ == "__main__":
    main()
    






