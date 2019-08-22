# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/13
# @Desc  : 
"""
scrapy模拟登陆
    1.直接携带cookies
        适用于cookie过期时间很长，常见于一些不规范的网站
        能在cookie过期之前把所有的数据拿到
        配合其他程序使用，比如使用selenium把登陆之后的cookie获取保存到本地，scrapy发送请求之前先读本地的cookie

        class RenrenSpider(scrapy.Spider):
            name = 'renren'
            cookies = dict(
                key: 'value',
            )

        def start_requests(self):   重写start_requests函数，指定start_urls的处理方式
            start_urls = 'http://www.renren.com/'
            yield scrapy.Request(start_urls, callback=self.parse, cookies=self.cookies)

        def parse(self, response):
            print(re.findall(r'毛**', response.body.decode())
            my_profile_url = 'http://www.renren.com/327550029/profile'
            yield scrapy.Request(my_profile_url, callback=self.parse_profile)

        def parse_profile(self, response):
            print(re.findall(r'毛**', response.body.decode()))

    2.找到发送post请求的url地址，带上信息，发送请求
        class GithubSpider(scrapy.Spider):
            name = 'github'
            allowed_domains = ['github.com']
            start_urls = ['https://github.com/login'] //请求首页，为了获取登陆参数
            headers = {
                ...
            }

            def parse(self, response):
                param1 = response.xpath('...')
                param2 = response.xpath('...')

                return scrapy.FormRequest("https://www.github.com/session", headers = self.headers, formdata=dict(
                    param1 = param1, param2 = param2), callback=self.after_login)

            def after_login(self, response):
                pass

"""

def main():
    pass


if __name__ == "__main__":
    main()
    






