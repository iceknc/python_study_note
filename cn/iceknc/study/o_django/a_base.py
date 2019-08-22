# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/15
# @Desc  : 
"""
准备虚拟环境
    python -m venv <name>
激活虚拟环境
    cd <name>\Scripts
        activate
        deactivate(停止虚拟环境)
安装django
    pip install django
创建项目
    django-admin startproject hello_django
        项目结构
            ----hello_django
                |----hello_django           项目的python模块
                |   |----__init__.py
                |   |----settings.py        项目的整体配置文件
                |   |----urls.py            项目的URL配置文件
                |   |----wsgi.py            项目与WSGI兼容的Web服务器入口
                |----manage.cfg             项目管理文件，通过它管理项目

创建应用
    使用一个应用开发一个业务模块
    python manage.py startapp first_app
        项目结构
            ----first_app
                |----migrations
                |   |----__init__.py
                |----__init__.py
                |----admin.py           跟网站的后台管理相关
                |----apps.py
                |----models.py          跟数据库操作相关
                |----tests.cfg          用于开发测试用例，在实际开发中会有专门的测试人员
                |----views.cfg          跟接收浏览器请求，进行处理，返回页面相关
安装应用
    应用创建成功后，需要安装才可以使用，也就是建立应用和项目之间的关联，在hello_django/settings.py中INSTALLED_APPS
    下添加应用的名称就可以完成安装。
开发服务器
    在开发阶段，为了能够快速预览到开发的效果，django提供了一个纯python编写的轻量级web服务器，仅在开发阶段使用
        python manage.py runserver
"""

import django

def main():
    print(django.VERSION)


if __name__ == "__main__":
    main()
