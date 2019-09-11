# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/6
# @Desc  : 
"""
中间件
    Django中的中间件是一个轻量级、底层的插件系统，可以介入Django的请求和响应处理过程，修改Django的输入或输出。
    中间件的设计为开发者提供了一种无侵入式的开发方式，增强了Django框架的健壮性，其它的MVC框架也有这个功能，名称为IoC。

    Django在中间件中预置了五个方法，这五个方法的区别在于不同的阶段执行，对输入或输出进行干预，方法如下：
        初始化：无需任何参数，服务器响应第一个请求的时候调用一次，用于确定是否启用当前中间件。
            def __init__(self, get_response):
                pass
        处理请求前：在每个请求上，request对象产生之后，url匹配之前调用，返回None或HttpResponse对象。
            def process_request(self, request):
                pass
        处理视图前：在每个请求上，url匹配之后，视图函数调用之前调用，返回None或HttpResponse对象。
            def process_view(self, request, view_func, *view_args, **view_kwargs):
                pass
        处理响应后：视图函数调用之后，所有响应返回浏览器之前被调用，在每个请求上调用，返回HttpResponse对象。
            def process_response(self, request, response):
                pass
        异常处理：当视图抛出异常时调用，在每个请求上调用，返回一个HttpResponse对象。
            def process_exception(self, request,exception):
                pass
    <项目名>/settings.py文件中,向MIDDLEWARE_CLASSES项中注册

    示例 <use_mysql>/<test_app>.middleware
"""

def main():
    pass


if __name__ == "__main__":
    main()
    






