# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/11
# @Desc  : 
"""
django使用redis存储session
    安装包
        pip install django-redis-sessions
    修改settings文件，增加如下项
        SESSION_ENGINE = 'redis_sessions.session'
        SESSION_REDIS_HOST = 'localhost'
        SESSION_REDIS_PORT = 6379
        SESSION_REDIS_DB = 2
        SESSION_REDIS_PASSWORD = ''
        SESSION_REDIS_PREFIX = 'session'


"""

def main():
    pass


if __name__ == "__main__":
    main()
    






