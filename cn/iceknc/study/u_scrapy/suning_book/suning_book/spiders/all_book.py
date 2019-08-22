# -*- coding: utf-8 -*-
import scrapy
import logging
from suning_book.items import SuningBookItem
from copy import deepcopy


class AllBookSpider(scrapy.Spider):
    name = 'all_book'
    allowed_domains = ['suning.com']
    start_urls = ['https://book.suning.com/?safp=d488778a.homepage1.99345513004.47']

    def parse(self, response):
        menu_list = response.xpath("//div[@class='submenu-left']")
        for menu_item in menu_list:
            class_name_list = menu_item.xpath("./p/a/text()")
            sub_class_list = menu_item.xpath("./ul")
            for sub_class_item in sub_class_list:
                sub_class_name_list = sub_class_item.xpath("./li/a")
                for item in sub_class_name_list:
                    book = SuningBookItem()
                    book["class_name"] = class_name_list[sub_class_list.index(sub_class_item)].extract()
                    book["sub_class_name"] = item.xpath("./text()").extract()[0]
                    cate_url = item.xpath("./@href").extract()[0]

                    print(book)

                    yield scrapy.Request(cate_url, callback=self.parse_class, meta={"book": deepcopy(book)})

    def parse_class(self, response):
        logging.debug("get class url:" + response.request.url)
        wrap_list = response.xpath("//div[@id='filter-results']/ul/li//div[@class='wrap']")
        print(response.meta["book"]["sub_class_name"] + " : " + response.request.url + "  item_count:" + str(len(wrap_list)))
        for wrap in wrap_list:
            #一页数据会显示60个，其中后面30个是监听滚动动态加载的数据，这里先不做后续处理了
            pass
