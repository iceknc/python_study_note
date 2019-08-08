# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentHrItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    position_english = scrapy.Field()
    position_chinese = scrapy.Field()
    base = scrapy.Field()
    date = scrapy.Field()
    desc = scrapy.Field()
