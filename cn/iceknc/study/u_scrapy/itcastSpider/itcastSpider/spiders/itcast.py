# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ajavaee']

    def parse(self, response):
        tea_class = response.xpath("//div[@class='tea_hd']//li/text()")
        tea_con = response.xpath("//div[@class='tea_con']/div")

        for cls in tea_class:
            tea_cls = tea_con[tea_class.index(cls)]
            tea_cls_list = tea_cls.xpath(".//li/div[@class='li_txt']")

            for each in tea_cls_list:
                item = ItcastspiderItem()
                # extract()方法返回的都是字符串
                name = each.xpath("h3/text()").extract()
                language = cls.extract()
                title = each.xpath("h4/text()").extract()
                info = each.xpath("p/text()").extract()

                # xpath返回的是包含一个元素的列表
                item['name'] = name[0]
                item['language'] = language
                item['title'] = title[0]
                item['info'] = info[0]
                yield item


class ItcastspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    language = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()
