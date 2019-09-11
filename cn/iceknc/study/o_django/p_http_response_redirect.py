# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/3
# @Desc  : 
"""
子类HttpResponseRedirect
    当一个逻辑处理完成后，不需要向客户端呈现数据，而是转回到其它页面，如添加成功、修改成功、删除成功后显示数据列表，
    而数据的列表视图已经开发完成，此时不需要重新编写列表的代码，而是转到这个视图就可以，此时就需要模拟一个用户请求的效果，
    从一个视图转到另外一个视图，就称为重定向。
    Django中提供了HttpResponseRedirect对象实现重定向功能，这个类继承自HttpResponse，被定义在django.http模块中，
    返回的状态码为302。

示例 <use_mysql>/<test_app>.views.redirect
"""

def main():
    pass


if __name__ == "__main__":
    main()
    






