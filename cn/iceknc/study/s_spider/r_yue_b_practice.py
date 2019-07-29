# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/7/29
# @Desc  :

import requests
from lxml import etree
import re
import os
import json

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed


def spider():
    result = {}

    url_list = []
    url_list.append("http://xqctk.jtys.sz.gov.cn/gbl/index.html")
    for i in range(15):
        url_list.append("http://xqctk.jtys.sz.gov.cn/gbl/index_{}.html".format(i + 2))

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}

    re_str = "深圳市(201[98765]年第\d{1,2}期)(普通小汽车|小汽车)增量指标摇号结果公告"

    for url in url_list:
        response = requests.get(url, headers=headers)

        html = etree.HTML(response.content)
        title = html.xpath('//div[@class="main_content"]//a[@class="text"]')
        for index, item in enumerate(title):
            decode = item.xpath("./text()")[0].encode("utf-8").decode()
            if re.match(re_str, decode):
                href = title[index]
                url = href.xpath("./@href")[0].encode("utf-8").decode()
                result[decode] = url

    for key in result:
        print("get --> " + key)
        response = requests.get(result[key], headers=headers)
        html = etree.HTML(response.content)
        a_list = html.xpath('//a')

        for item in a_list:
            text = item.xpath('./span/text()')
            if (len(text) > 0):
                if text[0].startswith(u"个人普通小汽车"):
                    href = item.xpath("./@href")
                    print("find --> " + re.match(re_str, key).group(1) + " " + text[0] + " : " + href[0])

                    download_request = requests.get(href[0], headers=headers)
                    file_name = "E://download/" + re.match(re_str, key).group(1) + ".pdf"
                    with open(file_name, "wb") as f:
                        f.write(download_request.content)
        print("\n")


def parse_file():
    listdir = os.listdir("E://download")

    for file in listdir:
        print(file)
        if not os.path.isfile("E://download/" + file):
            continue

        with open("E://download/" + file, 'rb') as f:
            # 用文件对象创建一个PDF文档分析器
            parser = PDFParser(f)
            # 创建一个PDF文档
            doc = PDFDocument()
            # 连接分析器，与文档对象
            parser.set_document(doc)
            doc.set_parser(parser)

            # 提供初始化密码，如果没有密码，就创建一个空的字符串
            doc.initialize()

            # 检测文档是否提供txt转换，不提供就忽略
            if not doc.is_extractable:
                raise PDFTextExtractionNotAllowed
            else:
                # 创建PDF，资源管理器，来共享资源
                rsrcmgr = PDFResourceManager()
                # 创建一个PDF设备对象
                laparams = LAParams()
                device = PDFPageAggregator(rsrcmgr, laparams=laparams)
                # 创建一个PDF解释其对象
                interpreter = PDFPageInterpreter(rsrcmgr, device)

                # 循环遍历列表，每次处理一个page内容
                # doc.get_pages() 获取page列表
                for page in doc.get_pages():
                    interpreter.process_page(page)
                    # 接受该页面的LTPage对象
                    layout = device.get_result()
                    # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象
                    # 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等
                    # 想要获取文本就获得对象的text属性，
                    for x in layout:
                        if (isinstance(x, LTTextBoxHorizontal)):
                            with open("E://download/parse/result.txt", 'a+', encoding="utf-8") as f:
                                results = x.get_text()
                                print(results)
                                f.write(results + "\n")


def clean_data():
    listdir = os.listdir("E://download/parse")

    with open("E://download/data/result.txt", 'a+', encoding="utf-8") as result:
        for file in listdir:
            print(file)
            with open("E://download/parse/" + file, 'r', encoding="utf-8") as f:
                readline = f.readlines()
                for line in readline:
                    if (line.startswith(u"本期编号")):
                        result.write(line)
                        continue
                    strip = line.strip()
                    if re.match("\d{1,4}\s+\d{13}\s+\D{2,6}", strip):
                        result.write(strip)
                        result.write("\n")
                result.write("\n")


def calc_result():
    result = {}
    with open("E://download/data/result.txt", 'r', encoding="utf-8") as f:
        readline = f.readlines()
        for line in readline:
            if (line.startswith(u"本期编号")):
                continue
            strip = line.strip()
            match = re.match("\d{1,4}\s+\d{13}\s+(\D{2,6})", strip)
            if match:
                name = match.group(1)
                if result.get(name) is not None:
                    result[name] += 1
                else:
                    result[name] = 1

                i = len(name)
                if i == 2:
                    if result.get("一个字的名字") is not None:
                        result["一个字的名字"] += 1
                    else:
                        result["一个字的名字"] = 1
                elif i == 3:
                    if result.get("两个字的名字") is not None:
                        result["两个字的名字"] += 1
                    else:
                        result["两个字的名字"] = 1
                else:
                    if result.get("其他类型的名字") is not None:
                        result["其他类型的名字"] += 1
                    else:
                        result["其他类型的名字"] = 1

    sort_result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    with open("E://download/data/result1.txt", "w+", encoding="utf-8") as  f:
        for item in sort_result:
            f.write(str(item))
            f.write("\n")


if __name__ == "__main__":
    # 1.抓取数据  有几个数据需要手动下载  xpath匹配不太好写
    # 具体可看文件对应的日期少了哪几个
    # spider()

    # 2.pdf 提取出文字 第三方库 pip install pdfminer3k
    # parse_file()

    # 3.初步清洗文字
    # clean_data()

    # 4.计算结果
    calc_result()
