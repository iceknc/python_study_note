# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/3
# @Desc  : 
"""
状态保持
    浏览器请求服务器是无状态的。无状态指一次用户请求时，浏览器、服务器无法知道之前这个用户做过什么，每次请求都是一次新的请求。
    无状态的应用层面的原因是：浏览器和服务器之间的通信都遵守HTTP协议。根本原因是：浏览器与服务器是使用Socket套接字进行通信的，
    服务器将请求结果返回给浏览器之后，会关闭当前的Socket连接，而且服务器也会在处理页面完毕之后销毁页面对象。
    有时需要保存下来用户浏览的状态，比如用户是否登录过，浏览过哪些商品等。 实现状态保持主要有两种方式：
        在客户端存储信息使用Cookie。
        在服务器端存储信息使用Session。

Cookie
    Cookie以键值对的格式进行信息的存储。
    Cookie基于域名安全，不同域名的Cookie是不能互相访问的。
    当浏览器请求某网站时，会将浏览器存储的跟网站相关的所有Cookie信息提交给网站服务器。

    设置Cookie
        def cookie_set(request):
            response = HttpResponse("<h1>设置Cookie，请查看响应报文头</h1>")
            response.set_cookie('h1', '你好')
            return response
        示例 <use_mysql>/<test_app>.views.cookie_set

    读取Cookie
        Cookie信息被包含在请求头中，使用request对象的COOKIES属性访问。
        def cookie_get(request):
            response = HttpResponse("读取Cookie，数据如下：<br>")
            if 'h1' in request.COOKIES:
                response.write('<h1>' + request.COOKIES['h1'] + '</h1>')
            return response
        示例 <use_mysql>/<test_app>.views.cookie_get

Session
    对于敏感、重要的信息，建议要储在服务器端，不能存储在浏览器中，如用户名、余额、等级、验证码等信息。
    在服务器端进行状态保持的方案就是Session

    启用Session
        Django项目默认启用Session。
        打开<项目名>/settings.py文件，在项MIDDLEWARE_CLASSES中启用Session中间件。
            'django.contrib.sessions.middleware.SessionMiddleware'
    存储方式
        打开<项目名>/settings.py文件，设置SESSION_ENGINE项指定Session数据存储的方式，可以存储在数据库、缓存、Redis等。
        存储在数据库中，如下设置可以写，也可以不写，这是默认存储方式。
            SESSION_ENGINE='django.contrib.sessions.backends.db'
        存储在缓存中：存储在本机内存中，如果丢失则不能找回，比数据库的方式读写更快。
            SESSION_ENGINE='django.contrib.sessions.backends.cache'
        混合存储：优先从本机内存中存取，如果没有则从数据库中存取。
            SESSION_ENGINE='django.contrib.sessions.backends.cached_db'
        如果存储在数据库中，需要在项INSTALLED_APPS中安装Session应用。
            'django.contrib.sessions'
    依赖于Cookie
        在使用Session后，会在Cookie中存储一个sessionid的数据，每次请求时浏览器都会将这个数据发给服务器，
        服务器在接收到sessionid后，会根据这个值找出这个请求者的Session。
        如果想使用Session，浏览器必须支持Cookie，否则就无法使用Session了。
        存储Session时，键与Cookie中的sessionid相同，值是开发人员设置的键值对信息，进行了base64编码，过期时间由开发人员设置。
    对象及方法
        以键值对的格式写session : request.session['键']=值
        根据键读取值 :  request.session.get('键',默认值)
        清除所有session，在存储中删除值部分 : request.session.clear()
        清除session数据，在存储中删除session的整条数据 : request.session.flush()
        删除session中的指定键及值，在存储中只删除某个键及对应的值 : del request.session['键']
        设置会话的超时时间，如果没有指定过期时间则两个星期后过期 : request.session.set_expiry(value)
            如果value是一个整数，会话将在value秒没有活动后过期。
            如果value为0，那么用户会话的Cookie将在用户的浏览器关闭时过期。
            如果value为None，那么会话永不过期
    示例 <use_mysql>/<test_app>.views.session_set
"""

def main():
    pass


if __name__ == "__main__":
    main()
    






