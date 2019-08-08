# -*- coding: utf-8 -*-
import scrapy
import logging


class AllBookSpider(scrapy.Spider):
    name = 'all_book'
    allowed_domains = ['suning.com']
    start_urls = ['https://book.suning.com/?safp=d488778a.homepage1.99345513004.47']

    def parse(self, response):
        menu_list = response.xpath("//div[@class='menu-item']")
        for menu_item in menu_list:
            class_url = menu_item.xpath("./dl/dt/h3/a/@href").extract()[0]
            class_name = menu_item.xpath("./dl/dt/h3/a/text()").extract()[0]
            logging.debug(class_url)
            if class_url.startswith("https://list.suning.com"):
                yield scrapy.Request(class_url, callback=self.parse_class, meta={"class": class_name})
            else:
                logging.debug("舍弃地址：" + class_url)

    def parse_class(self, response):
        wrap_list = response.xpath("//div[@id='filter-results']/ul/li")
        print(response.meta["class"] + " : " + response.request.url + "  item_count:" + str(len(wrap_list)))
        for wrap in wrap_list:
            pass
