# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/28
# @Desc  :
"""
数据库操作
    查看所有数据库
        show databases;
    使用数据库
        use 数据库名;
    查看当前使用的数据库
        select database();
    创建数据库
        create database 数据库名 charset=utf8;
    删除数据库
        drop database 数据库名;
    备份
        mysqldump –uroot –p 数据库名 > 备份文件名;
    恢复
        mysql -uroot –p 新数据库名 < 备份文件名

数据表操作
    查看当前数据库中所有表
        show tables;
    查看表结构
        desc 表名;
    创建表
        auto_increment表示自动增长
        CREATE TABLE table_name(
            column1 datatype contrai,
            column2 datatype,
            column3 datatype,
            .....
            columnN datatype,
            PRIMARY KEY(one or more columns)
        );
    修改表-添加字段
        alter table 表名 add 列名 类型;
    修改表-修改字段：重命名版
        alter table 表名 change 原名 新名 类型及约束;
    修改表-修改字段：不重命名版
        alter table 表名 modify 列名 类型及约束;
    修改表-删除字段
        alter table 表名 drop 列名;、
    删除表
        drop table 表名;
    查看表的创建语句
        show create table 表名;

数据操作
    查询所有列
        select * from 表名;
    查询指定列，可以使用as为列或表指定别名
        select 列1,列2,... from 表名;

    全列插入：值的顺序与表中字段的顺序对应，主键列是自动增长，但是在全列插入时需要占位，
    通常使用0或者 default 或者 null 来占位，插入成功后以实际数据为准
        insert into 表名 values(...)
    部分列插入：值的顺序与给出的列顺序对应
        insert into 表名(列1,...) values(值1,...)

    修改
        update 表名 set 列1=值1,列2=值2... where 条件

    删除
        delete from 表名 where 条件

    逻辑删除，本质就是修改操作
        update 表名 set isdelete=1 where 条件;
"""


def main():
    pass


if __name__ == "__main__":
    main()
    






