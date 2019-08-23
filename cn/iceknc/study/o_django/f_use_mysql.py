# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/22
# @Desc  : 
"""
django默认使用sqlite3数据库，要切换到mysql，做如下配置
    打开 <项目名>/settings.py文件，找到DATABASES项
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'test2', #数据库名字，
                'USER': 'root', #数据库登录用户名
                'PASSWORD': 'mysql', #数据库登录密码
                'HOST': 'localhost', #数据库所在主机
                'PORT': '3306', #数据库端口
            }
        }
    Django框架不会自动生成数据库，需要我们自己进入mysql数据库去创建

    安装pymysql模块
        pip install pymysql

    配置模块
        打开 <项目名>/__init__.py文件, 添加
            import pymysql
            pymysql.install_as_MySQLdb()

"""

def main():
    pass


if __name__ == "__main__":
    main()
    






