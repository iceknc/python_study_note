# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/21
# @Desc  : 
"""
后台管理
    使用Django的管理模块，需要按照如下步骤操作
        管理界面本地化
            本地化是将显示的语言、时间等使用本地的习惯，这里的本地化就是进行中国化，中国大陆地区使用简体中文，时区使用亚洲/上海时区，
            注意这里不使用北京时区表示。

            打开hello_django/settings.py文件，找到语言编码、时区的设置项，将内容改为如下：
                LANGUAGE_CODE = 'zh-hans' #使用中国语言
                TIME_ZONE = 'Asia/Shanghai' #使用中国上海时间

        创建管理员
            创建管理员的命令如下，按提示输入用户名、邮箱、密码
                python manage.py createsuperuser
            接下来启动服务器
                python manage.py runserver
            打开浏览器，在地址栏中输入如下地址后回车
                http://127.0.0.1:8000/admin/

        注册模型类
            登录后台管理后，默认没有我们创建的应用中定义的模型类，需要在自己应用中的admin.py文件中注册，才可以在后台管理中看到，
            并进行增删改查操作。
            打开first_app/admin.py文件，编写如下代码：
                from django.contrib import admin
                from first_app.models import BookInfo,HeroInfo

                admin.site.register(BookInfo)
                admin.site.register(HeroInfo)
            到浏览器中刷新页面，可以看到模型类BookInfo和HeroInfo的管理了

        自定义管理页面
            在列表页只显示出了BookInfo object，对象的其它属性并没有列出来，查看非常不方便。 Django提供了自定义管理页面的功能，
            比如列表页要显示哪些值
            打开first_app/admin.py文件，自定义类，继承自admin.ModelAdmin类。
                属性list_display表示要显示哪些属性
                class BookInfoAdmin(admin.ModelAdmin):
                    list_display = ['id', 'btitle', 'bpub_date']
                修改模型类BookInfo的注册代码如下
                    admin.site.register(BookInfo, BookInfoAdmin)

"""

def main():
    pass


if __name__ == "__main__":
    main()
    






