# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SuningBookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    class_name = scrapy.Field()
    sub_class_name = scrapy.Field()
    cate_url = scrapy.Field()
