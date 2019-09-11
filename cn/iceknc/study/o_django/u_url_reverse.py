# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/5
# @Desc  : 
"""
反向解析
    随着功能的增加会出现更多的视图，可能之前配置的正则表达式不够准确，于是就要修改正则表达式，但是正则表达式一旦修改了，
    之前所有对应的超链接都要修改，真是一件麻烦的事情，而且可能还会漏掉一些超链接忘记修改，有办法让链接根据正则表达式动态生成吗？
    答：反向解析。
    反向解析应用在两个地方：模板中的超链接，视图中的重定向。

    要实现反向解析功能，需要如下步骤:
        在<项目名>/urls.py中为include定义namespace属性
            url(r'^',include('<应用名>.urls',namespace='<应用名或者自定义名>')),
        在<应用名>/urls.py中为应用定义app_name属性
            app_name = '[<应用名或者自定义名>]'  #跟上一步的名字保持要一致
        在<应用名>/urls.py中为url定义name属性
            url(r'^index/$', views.index,name='<url名字>'),
            url(r'^index/(\d+)$', views.index,name='<url名字>'),
            url(r'^index/(?P<p1>\d+)/(?P<p2>\d+)$', views.index,name='<url名字>'),
        在模板中使用url标签做超链接
            href="{%url '<应用名或者自定义名>:<url名字>'%}
            href="{%url '<应用名或者自定义名>:<url名字>' <parama1> <parama2>%}
            href="{%url '<应用名或者自定义名>:<url名字>' p1=v1 p2=v2%}
        在视图中使用
            from django.urls import reverse
            def code_reverse(request):
                # url = reverse('<应用名或者自定义名>:<url名字>')
                # url = reverse('<应用名或者自定义名>:<url名字>', args=(p1,))
                url = reverse('<应用名或者自定义名>:<url名字>', kwargs={'p1': v1, 'p2': v2})
                return red(url)
"""

def main():
    pass


if __name__ == "__main__":
    main()
    






