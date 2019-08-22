# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/21
# @Desc  : 
"""
视图
    使用视图时需要进行两步操作
        定义视图 : 视图就是一个Python函数，被定义在views.py中
            视图的必须有一个参数，一般叫request，视图必须返回HttpResponse对象，HttpResponse中的参数内容会显示在浏览器的页面上。
                打开first_app/views.py文件，定义视图index如下
                    from django.http import HttpResponse

                    def index(request):
                        return HttpResponse("index")

        配置URLconf
            请求者在浏览器地址栏中输入url，请求到网站后，获取url信息，然后与编写好的URLconf逐条匹配，如果匹配成功则调用对
            应的视图函数，如果所有的URLconf都没有匹配成功，则返回404错误

            一条URLconf包括url规则、视图两部分
                url规则使用正则表达式定义。
                视图就是在views.py中定义的视图函数

            需要两步完成URLconf配置
                在应用中定义URLconf
                    打开first_app/应用下创建urls.py文件，定义代码如下
                    from django.conf.urls import url
                    from 打开first_app import views
                    urlpatterns = [
                        url(r'^$', views.index),
                    ]
                包含到项目中：打开打开hello_django/urls.py文件，为urlpatterns列表增加项如下

        请求访问
            视图和URLconf都定义好了，接下来在浏览器地址栏中输入网址
                http://127.0.0.1:8000/
"""

def main():
    pass


if __name__ == "__main__":
    main()
    






