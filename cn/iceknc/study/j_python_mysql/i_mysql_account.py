# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/30
# @Desc  : 
"""
账户管理
    在生产环境下操作数据库时，绝对不可以使用root账户连接，而是创建特定的账户，授予这个账户特定的操作权限，
    然后连接进行操作，主要的操作就是数据的crud

    MySQL账户体系：根据账户所具有的权限的不同，MySQL的账户可以分为以下几种
        服务实例级账号：启动了一个mysqld，即为一个数据库实例；如果某用户如root,拥有服务实例级分配的权限，
        那么该账号就可以删除所有的数据库、连同这些库中的表
        数据库级别账号：对特定数据库执行增删改查的所有操作
        数据表级别账号：对特定表执行增删改查等所有操作
        字段级别的权限：对某些表的特定字段进行操作
        存储程序级别的账号：对存储程序进行增删改查的操作

    账户的操作主要包括创建账户、删除账户、修改密码、授权权限等

    注意:
        进行账户操作时，需要使用root账户登录，这个账户拥有最高的实例级权限
        通常都使用数据库级操作权限

    查看所有用户
        所有用户及权限信息存储在mysql数据库的user表中
        查看user表的结构
            desc user;
        主要字段说明
            Host表示允许访问的主机
            User表示用户名
            authentication_string表示密码，为加密后的值
        查看所有用户
            select host,user,authentication_string from user;

     创建账户、授权
        需要使用实例级账户登录后操作，以root为例
        常用权限主要包括：create、alter、drop、insert、update、delete、select
        如果分配所有权限，可以使用all privileges

        grant 权限列表 on 数据库 to '用户名'@'访问主机' identified by '密码';

        查看用户有哪些权限
            show grants for 用户名;

        修改权限
            grant 权限名称 on 数据库 to 账户@主机 with grant option;

        修改密码
            update user set authentication_string=password('新密码') where user='用户名';
            修改完成后需要刷新权限
                flush privileges

        删除账户
            drop user '用户名'@'主机';
            使用root登录，删除mysql数据库的user表中数据
                delete from user where user='用户名';

"""

def main():
    pass


if __name__ == "__main__":
    main()
    






