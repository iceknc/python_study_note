# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/7
# @Desc  : 
"""
Item Pipeline
    当Item在Spider中被收集之后，它将会被传递到Item Pipeline，这些Item Pipeline组件按定义的顺序处理Item。
    每个Item Pipeline都是实现了简单方法的Python类，比如决定此Item是丢弃而存储。以下是item pipeline的一些典型应用：
        验证爬取的数据(检查item包含某些字段，比如说name字段)
        查重(并丢弃)
        将爬取结果保存到文件或者数据库中

    编写item pipeline
        item pipiline组件是一个独立的Python类，其中process_item()方法必须实现

    启用一个Item Pipeline组件
        为了启用Item Pipeline组件，必须将它的类添加到 settings.py文件ITEM_PIPELINES 配置，就像下面这个例子:
        # Configure item pipelines
        # See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
        ITEM_PIPELINES = {
            #'mySpider.pipelines.SomePipeline': 300,
            "mySpider.pipelines.ItcastJsonPipeline":300
        }
        分配给每个类的整型值，确定了他们运行的顺序，item按数字从低到高的顺序，通过pipeline，
        通常将这些数字定义在0-1000范围内（0-1000随意设置，数值越低，组件的优先级越高）
"""

def main():
    pass


if __name__ == "__main__":
    main()
    






