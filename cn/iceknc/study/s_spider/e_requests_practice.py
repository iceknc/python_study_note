# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/7/23
# @Desc  : 

import requests


class FundSpider(object):
    """
    天天基金网的基金排行爬虫
    """

    def __init__(self):
        self.url_temp = 'http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=zzf&st=desc&sd=' \
                        '2018-07-23&ed=2019-07-23&qdii=&tabSubtype=,,,,,&pi={}&pn=50&dx=1&v=0.14019299221900583'
        self.header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}

    def get_url_list(self):
        return [self.url_temp.format(i) for i + 1 in range(103)]

    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.header)
        return response.content.decode()

    def save_data(self, data_str, page_num):
        with open('fund_data.txt', 'a+', encoding='utf8') as f:
            f.write(str(page_num) + "  --> " + data_str)
            f.write("\n")

    def run(self):
        url_list = self.get_url_list()
        for url in url_list:
            data_response = self.parse_url(url)
            page_num = url_list.index(url) + 1
            self.save_data(data_response, page_num)


def main():
    spider = FundSpider()
    spider.run()


if __name__ == "__main__":
    main()
