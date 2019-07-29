# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/7/26
# @Desc  : 
"""
lxml库
    lxml 是 一个HTML/XML的解析器，主要的功能是如何解析和提取 HTML/XML 数据。
    lxml和正则一样，也是用 C 实现的，是一款高性能的 Python HTML/XML 解析器，
    我们可以利用之前学习的XPath语法，来快速的定位特定元素以及节点信息

    lxml 可以自动修正 html 代码，但是也有可能出现错误的情况
"""

from lxml import etree


def main():
    text = '''
    <div>
        <ul>
             <li class="item-0"><a href="link1.html">first item</a></li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-inactive"><a href="link3.html">third item</a></li>
             <li class="item-1"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a>
         </ul>
     </div>
    '''

    html = etree.HTML(text)
    print(etree.tostring(html, pretty_print=True).decode())

    parse = etree.parse("hello.html")
    print(etree.tostring(parse).decode())

    # 获取所有的 <li> 标签
    result = html.xpath("//li")
    print("-" * 30)
    print(result)

    # 获取<li> 标签的所有 class属性
    result = html.xpath("//li/@class")
    print("-" * 30)
    print(result)

    # 继续获取<li>标签下hre 为 link1.html 的 <a> 标签
    result = html.xpath('//li/a[@href="link1.html"]')
    print("-" * 30)
    print(result)

    # 获取 < li > 标签下的所有 < span > 标签
    # result = html.xpath('//li/span')
    # 注意这么写是不对的：
    # 因为 / 是用来获取子元素的，而 <span> 并不是 <li> 的子元素，所以，要用双斜杠
    result = parse.xpath('//li//span')
    print("-" * 30)
    print(result)

    # 获取 <li> 标签下的<a>标签里的所有 class
    result = parse.xpath('//li/a//@class')
    print("-" * 30)
    print(result)

    # 获取最后一个 <li> 的 <a> 的 href
    result = parse.xpath('//li[last()]/a/@href')
    # 谓语 [last()] 可以找到最后一个元素
    print("-" * 30)
    print(result)

    # 获取倒数第二个元素的内容
    result = parse.xpath('//li[last()-1]/a')
    print("-" * 30)
    print(result)

    # 获取 class 值为 bold 的标签名
    result = parse.xpath("//*[@class='bold']")
    print("-" * 30)
    print(result)


if __name__ == "__main__":
    main()
