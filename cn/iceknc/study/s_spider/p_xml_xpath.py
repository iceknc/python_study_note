# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/7/25
# @Desc  : 
"""
<?xml version="1.0" encoding="utf-8"?>
<bookstore>
    <book>
        <title>Harry Potter</title>
        <author>J K. Rowling</author>
        <year>2005</year>
        <price>29.99</price>
    </book>
</bookstore>

XML的节点关系
    1. 父（Parent） 每个元素以及属性都有一个父
        book 元素是 title、author、year 以及 price 元素的父
    2. 子（Children） 元素节点可有零个、一个或多个子
        title、author、year 以及 price 元素都是 book 元素的子
    3. 同胞（Sibling） 拥有相同的父的节点
        title、author、year 以及 price 元素都是同胞
    4. 先辈（Ancestor） 某节点的父、父的父，等等
        title 元素的先辈是 book 元素和 bookstore 元素
    5. 后代（Descendant  某个节点的子，子的子，等等
        bookstore 的后代是 book、title、author、year 以及 price 元素

XPath (XML Path Language)
    一门在 XML 文档中查找信息的语言，可用来在 XML 文档中对元素和属性进行遍历

    XPath 开发工具
        开源的XPath表达式编辑工具:XMLQuire(XML格式文件可用)
        Chrome插件 XPath Helper
        Firefox插件 XPath Checker

    选取节点
        nodename   选取此节点的所有子节点
          /        从根节点选取
          //       从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置
          .        选取当前节点
          ..       选取当前节点的父节点
          @        选取属性

        a/text()        获取a标签的文本
        a//text()       获取a标签下的所有标签的文本
        a/@href         获取a标签的href
        //ul[@id="x"]   获取id为x的ul
        li//a           li下任何一个a标签

    谓语（Predicates） 谓语用来查找某个特定的节点或者包含某个指定的值的节点，被嵌在方括号中
        /bookstore/book[1] 	                选取属于 bookstore 子元素的第一个 book 元素。
        /bookstore/book[last()] 	        选取属于 bookstore 子元素的最后一个 book 元素。
        /bookstore/book[last()-1] 	        选取属于 bookstore 子元素的倒数第二个 book 元素。
        /bookstore/book[position()<3] 	    选取最前面的两个属于 bookstore 元素的子元素的 book 元素。
        //title[@lang] 	                    选取所有拥有名为 lang 的属性的 title 元素。
        //title[@lang=’eng’] 	            选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。
        /bookstore/book[price>35.00] 	    选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值须大于 35.00。
        /bookstore/book[price>35.00]/title 	选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00。

    选取未知节点
        * 	    匹配任何元素节点。
        @* 	    匹配任何属性节点。
        node() 	匹配任何类型的节点。

        /bookstore/* 	        选取 bookstore 元素的所有子元素。
        //* 	                选取文档中的所有元素。
        html/node()/meta/@* 	选择html下面任意节点下的meta节点的所有属性
        //title[@*] 	        选取所有带有属性的 title 元素。

    选取若干路径  通过在路径表达式中使用“|”运算符，您可以选取若干个路径
        //book/title | //book/price 	    选取 book 元素的所有 title 和 price 元素。
        //title | //price 	                选取文档中的所有 title 和 price 元素。
        /bookstore/book/title | //price 	选取属于 bookstore 元素的 book 元素的所有 title 元素，以及文档中所有的 price 元素。

    XPath的运算符
        |   计算两个节点集      //book|//cd               返回所有拥有book和cd元素的节点集
        +   加法               6+4                          10
        -   减法               6-4                           2
        *   乘法               6*4                          24
        div 除法               8 div 4                       2
        =   等于               price=9.8                 返回true/false
        !=  不等于             price!=9.8                返回true/false
        <   小于               price<9.8                 返回true/false
        <=  小于或等于          price<=9.8                返回true/false
        >   大于                price>9.8                 返回true/false
        >=  大于或等于           price>=9.8                返回true/false
        or  或                  price=9.8 or price=9.7    返回true/false
        and 与                  price<9.8 and price>9.7   返回true/false
        mod 余数                 5 mod 2                       1
"""

def main():
    pass


if __name__ == "__main__":
    main()
    






