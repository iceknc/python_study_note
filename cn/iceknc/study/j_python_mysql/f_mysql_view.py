# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/29
# @Desc  :

"""
视图
    视图就是一条SELECT语句执行后返回的结果集。所以我们在创建视图的时候，主要的工作就落在创建这条SQL查询语句上
    视图是对若干张基本表的引用，一张虚表，查询语句执行的结果，不存储具体的数据（基本表数据发生了改变，视图也会跟着改变）
    方便操作，特别是查询操作，减少复杂的SQL语句，增强可读性

定义视图
    create view 视图名称 as select语句;  建议以v_开头
查看视图
    show tables;  查看表会将所有的视图也列出来
使用视图
    select * from v_stu_score;   视图的用途就是查询
删除视图
    drop view 视图名称;
"""


def main():
    pass


if __name__ == "__main__":
    main()
    






