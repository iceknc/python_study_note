# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/2
# @Desc  : 
"""
视图
    视图就是python中的函数，视图一般被定义在"<应用>/views.py"文件中。视图必须返回一个HttpResponse对象或子对象作为响应。
    响应可以是一张网页的HTML内容，一个重定向，一个404错误等。
    视图的第一个参数必须为HttpRequest实例，还可能包含下参数如：
        通过正则表达式组获得的关键字参数。
        通过正则表达式组获取的位置参数
内置错误视图
    Django内置处理HTTP错误的视图，主要错误及视图包括：
        404错误：page not found视图
            将请求地址进行url匹配后，没有找到匹配的正则表达式，则调用404视图，这个视图会调用404.html的模板进行渲染。
            视图传递变量request_path给模板，表示导致错误的URL。
        500错误：server error视图
            在视图中代码运行报错会发生500错误，调用内置错误视图，使用templates/500.html模板渲染。
    如果想看到错误视图而不是调试信息，需要修改<项目名>/setting.py文件的DEBUG项。
        DEBUG = False
        ALLOWED_HOSTS = ['*', ]
"""

def main():
    pass


if __name__ == "__main__":
    main()
    






