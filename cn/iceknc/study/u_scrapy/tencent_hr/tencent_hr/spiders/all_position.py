# -*- coding: utf-8 -*-
import scrapy
from tencent_hr.items import TencentHrItem

class AllPositionSpider(scrapy.Spider):
    name = 'all_position'
    allowed_domains = ['tencent.com']
    start_urls = ['https://careers.tencent.com/search.html']

    def parse(self, response):
        print(response.text)
        list = response.xpath("//div[@class='recruit-list']")
        print(len(list))
        for position_item in list:
            item = TencentHrItem()

            item["title"] = position_item.xpath("h4/text()").extract()[0]

            tip_list = position_item.xpath("p/span")
            item["position_english"] = tip_list[1].xpath("./text()").extract()[0]
            item["base"] = tip_list[2].xpath("./text()").extract()[0]
            item["position_chinese"] = tip_list[3].xpath("./text()").extract()[0]
            item["date"] = tip_list[4].xpath("./text()").extract()[0]

            item["desc"] = position_item.xpath("p[@class='recruit-txt']/text()").extract()[0]

            yield item

