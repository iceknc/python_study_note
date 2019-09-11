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
                from test_app.models import BookInfo,HeroInfo

                admin.site.register(BookInfo)
                admin.site.register(HeroInfo)
            到浏览器中刷新页面，可以看到模型类BookInfo和HeroInfo的管理了

        自定义管理页面
            在列表页只显示出了BookInfo object，对象的其它属性并没有列出来，查看非常不方便。 Django提供了自定义管理页面的功能，
            比如列表页要显示哪些值
            打开first_app/admin.py文件，自定义类，继承自admin.ModelAdmin类。
                class BookInfoAdmin(admin.ModelAdmin):
                    list_display = ['id', 'btitle', 'bpub_date']  #表示要显示哪些属性
                        列可以是模型字段，还可以是模型方法，要求方法有返回值。
                            short_description='列标题'  #列标题默认为属性或方法的名称，可以通过属性设置方法的显示名字。
                    list_per_page=100  #每页中显示多少条数据，默认为每页显示100条数据
                    actions_on_top=True  #顶部显示的属性，设置为True在顶部显示，设置为False不在顶部显示，默认为True。
                    actions_on_bottom=False #底部显示的属性，设置为True在底部显示，设置为False不在底部显示，默认为False。
                    ordering=['字段1','-字段2'] #定排序依据。 字段前面加负号表示逆序
                    list_filter=[] #右侧栏过滤器,会将对应字段的值列出来，用于快速过滤。
                    search_fields=[] #搜索框,于对指定字段的值进行搜索，支持模糊查询。
                修改模型类BookInfo的注册代码如下
                    admin.site.register(BookInfo, BookInfoAdmin)
            中文标题
                打开first_app/models.py文件，修改模型类，为属性指定verbose_name参数，即第一个参数。
                    atitle=models.CharField('标题',max_length=30)#名称
                    short_description='列标题'  #列标题默认为属性或方法的名称，可以通过属性设置方法的显示名字。
        编辑页选项
            显示字段顺序
                属性：fields=[]
            修改关联属性的显示，在关联类中添加str方法
                def __str__(self):
                    return "xxx"
            分组显示
                属性：fieldset=(
                        ('组1标题',{'fields':('字段1','字段2')}),
                        ('组2标题',{'fields':('字段3','字段4')}),
                     )
            关联对象
                在一对多的关系中，可以在一端的编辑页面中编辑多端的对象，嵌入多端对象的方式包括表格、块两种。
                类型InlineModelAdmin：表示在模型的编辑页面嵌入关联模型的编辑。
                子类TabularInline：以表格的形式嵌入。
                    打开<应用名>/admin.py文件，创建XxxTabularInline类。
                        class XxxTabularInline(admin.TabularInline):
                            model = XXXX #写多类的名字
                            extra = 2 #额外编辑2个子对象
                    打开<应用名>/admin.py文件，修改一类的Admin类如下：
                        classYyyyAdmin(admin.ModelAdmin):
                            ...
                            inlines = [XxxTabularInline]
                子类StackedInline：以块的形式嵌入。
                    打开<应用名>/admin.py文件，创建XxxStackedInline类。
                        class XxxStackedInline(admin.StackedInline):
                            model = XXXX #写多类的名字
                            extra = 2 #额外编辑2个子对象
                    打开<应用名>/admin.py文件，修改一类的Admin类如下：
                        classYyyyAdmin(admin.ModelAdmin):
                            ...
                            inlines = [XxxStackedInline]


"""

def main():
    pass


if __name__ == "__main__":
    main()
    






