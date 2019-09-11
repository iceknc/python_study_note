# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/2
# @Desc  : 
"""
URLconf
    用户通过在浏览器的地址栏中输入网址请求网站，对于Django开发的网站，由哪一个视图进行处理请求，是由url匹配找到的。
配置
    在<项目名>/settings.py中通过ROOT_URLCONF指定url配置，默认已经有此配置
        ROOT_URLCONF = '<项目名>.urls'
    打开<项目名>/urls.py可以看到默认的配置
        urlpatterns = [
            url{r'^admin/', include(admin.site.urls)),}
        ]
    注意点
        在<项目名>/urls.py中进行包含配置，在各自应用中创建具体配置。
        定义urlpatterns列表，存储url()对象，这个名称是固定的。
语法
    url()对象，被定义在django.conf.urls包中，有两种语法结构：
        语法一：包含，一般在自定义应用中创建一个urls.py来定义url。
            这种语法用于<项目名>/urls.py中，目的是将应用的urls配置到应用内部，数据更清晰并且易于维护。
                url(正则,include('<应用>.urls'))
        语法二：定义，指定URL和视图函数的对应关系。
            在应用内部创建urls.py文件，指定请求地址与视图的对应关系。
                url(正则,'视图函数名称')
        说明1：正则部分推荐使用r，表示字符串不转义，这样在正则表达式中使用\只写一个就可以。
        说明2：不能在开始加反斜杠，推荐在结束加反斜杠。
            正确：index/
            正确：index
            错误：/index
            错误：/index/
获取值
    请求的url被看做是一个普通的python字符串，进行匹配时不包括域名、get或post参数。 如请求地址如下:
        http://127.0.0.1:8000/delete/1/?a=10
    去除掉域名和参数部分，并将最前面的/去除后，只剩下如下部分与正则匹配:
        delete/1/
    定义与这个地址匹配的url如下：
        url(r'^delete/(\+d+)/$', views.delete)
    在<应用>/views.py中创建视图delete
        def delete(request, id):
            return HttpResponse('delete')

    获取值需要在正则表达式中使用小括号，分为两种方式：
        位置参数
            直接使用小括号，通过位置参数传递给视图,如上面几行
        关键字参数
            在正则表达式部分为组命名:  url(r'^delete/(?P<id>\d+)/$',views.delete)
            其中?P部分表示为这个参数定义的名称为id，可以是其它名称，起名做到见名知意
            视图delete此时必须要有一个参数名为id1，否则报错
        注意：两种参数的方式不要混合使用，在一个正则表达式中只能使用一种参数方式
"""

def main():
    pass


if __name__ == "__main__":
    main()
    






