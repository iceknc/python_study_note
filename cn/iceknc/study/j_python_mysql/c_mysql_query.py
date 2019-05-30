# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/28
# @Desc  :
"""
使用where子句对表中的数据筛选，结果为true的行会出现在结果集中

比较运算符
    等于: =
    大于: >
    大于等于: >=
    小于: <
    小于等于: <=
    不等于: != 或 <>

逻辑运算符
    and
    or
    not

模糊查询
    like
        select * from students where name like '黄%';  查询姓黄的学生
    %表示任意多个任意字符
        select * from students where name like '黄%' or name like '%靖'; 查询姓黄或叫靖的学生
    _表示一个任意字符
        select * from students where name like '黄_'; 查询姓黄并且“名”是一个字的学生

范围查询
    in 表示在一个非连续的范围内
        select * from students where id in(1,3,8); 查询编号是1或3或8的学生
    between ... and .. 表示在一个连续的范围内
        select * from students where id between 3 and 8; 查询编号为3至8的学生
        select * from students where (id between 3 and 8) and gender=1;  查询编号是3至8的男生

空判断
    注意：null与''是不同的
    判空is null
        select * from students where height is null; 查询没有填写身高的学生
    判非空is not null
        select * from students where height is not null; 查询填写了身高的学生

优先级
    优先级由高到低的顺序为：小括号，not，比较运算符，逻辑运算符
    and比or先运算，如果同时出现并希望先算or，需要结合()使用

排序
    select * from 表名 order by 列1 asc|desc [,列2 asc|desc,...]

    将行数据按照列1进行排序，如果某些行列1的值相同时，则按照列2排序，以此类推
    默认按照列值从小到大排列（asc）
    asc从小到大排列，即升序
    desc从大到小排序，即降序

聚合函数
    总数
        count(*)表示计算总行数，括号中写星与列名，结果是相同的
            select count(*) from students;  查询学生总数
    最大值
        max(列)表示求此列的最大值
            select max(id) from students where gender=2; 查询女生的编号最大值
    最小值
        min(列)表示求此列的最小值
            select min(id) from students where is_delete=0;  查询未删除的学生最小编号
    求和
        sum(列)表示求此列的和
            select sum(age) from students where gender=1; 查询男生的总年龄
    平均值
        avg(列)表示求此列的平均值
            select avg(id) from students where is_delete=0 and gender=2; 查询未删除女生的编号平均值

分组
    +----+-----------+------+--------+--------+--------+-----------+
    | id | name      | age  | height | gender | cls_id | is_delete |
    +----+-----------+------+--------+--------+--------+-----------+
    |  1 | xiaoming  |   18 | 180.00 | female |      1 |           |
    |  2 | xiaoyue   |   18 | 180.00 | female |      2 |           |
    |  3 | pengyuyan |   29 | 185.00 | male   |      1 |           |
    |  4 | liudehua  |   59 | 175.00 | male   |      2 |           |
    |  5 | huangrong |   38 | 160.00 | female |      1 |           |
    |  6 | fengjie   |   28 | 150.00 | secret |      2 |           |
    |  7 | wangzuxian|   18 | 172.00 | female |      1 |           |
    |  8 | jielun    |   36 |   NULL | male   |      1 |           |
    |  9 | chengkun  |   27 | 181.00 | male   |      2 |           |
    | 10 | liuyifei  |   25 | 166.00 | female |      2 |           |
    | 11 | jinxing   |   33 | 162.00 | ladyboy|      3 |           |
    | 12 | jingxiang |   12 | 180.00 | female |      4 |           |
    | 13 | zhoujie   |   34 | 176.00 | female |      5 |           |
    | 14 | guojing   |   12 | 170.00 | male   |      4 |           |
    +----+-----------+------+--------+--------+--------+-----------+
    group by
        将查询结果按照1个或多个字段进行分组，字段值相同的为一组
            select gender from students group by gender;
            +--------+
            | gender |
            +--------+
            | male   |
            | female |
            | ladyboy|
            | secret |
            +--------+
    group by + group_concat()
        group_concat(字段名) 可以作为一个输出字段来使用
        表示分组之后，根据分组结果，使用group_concat()来放置每一组的某字段的值的集合
            select gender,group_concat(id) from students group by gender;
            +--------+------------------+
            | gender | group_concat(id) |
            +--------+------------------+
            | male   | 3,4,8,9,14       |
            | female | 1,2,5,7,10,12,13 |
            | ladyboy| 11               |
            | secret | 6                |
            +--------+------------------+
    group by + 集合函数
        我们既然可以统计出每个分组的某字段的值的集合，那么我们也可以通过集合函数来对这个值的集合做一些操作
            select gender,avg(age) from students group by gender;
            +--------+----------+
            | gender | avg(age) |
            +--------+----------+
            | male   |  32.6000 |
            | female |  23.2857 |
            | ladyboy|  33.0000 |
            | secret |  28.0000 |
            +--------+----------+
    group by + having
        having 条件表达式：用来分组查询后指定一些条件来输出查询结果
        having作用和where一样，但having只能用于group by
            select gender,count(*) from students group by gender having count(*)>2;
            +--------+----------+
            | gender | count(*) |
            +--------+----------+
            | male   |        5 |
            | female |        7 |
            +--------+----------+
    group by + with rollup
        with rollup的作用是：在最后新增一行，来记录当前列里所有记录的总和
            select gender,count(*) from students group by gender with rollup;
            +--------+----------+
            | gender | count(*) |
            +--------+----------+
            | male   |        5 |
            | female |        7 |
            | ladyboy|        1 |
            | secret |        1 |
            | NULL   |       14 |
            +--------+----------+

            select gender,group_concat(age) from students group by gender with rollup;
            +--------+-------------------------------------------+
            | gender | group_concat(age)                         |
            +--------+-------------------------------------------+
            | male   | 29,59,36,27,12                            |
            | female | 18,18,38,18,25,12,34                      |
            | ladyboy| 33                                        |
            | secret | 28                                        |
            | NULL   | 29,59,36,27,12,18,18,38,18,25,12,34,33,28 |
            +--------+-------------------------------------------+

分页
    获取部分行
        select * from 表名 limit start,count
            从start开始，获取count条数据
            select * from students where gender=1 limit 0,3; 查询前3行男生信息

    已知：每页显示m条数据，当前显示第n页
    求总页数：此段逻辑后面会在python中实现
        查询总条数p1
        使用p1除以m得到p2
        如果整除则p2为总数页
        如果不整除则p2+1为总页数
    求第n页的数据
        select * from students where is_delete=0 limit (n-1)*m,m

连接查询
    当查询结果的列来源于多张表时，需要将多张表连接成一个大的数据集，再选择合适的列返回
    mysql支持三种类型的连接查询，分别为：
        内连接查询：查询的结果为两个表匹配到的数据
        右连接查询：查询的结果为两个表匹配到的数据，右表特有的数据，对于左表中不存在的数据使用null填充
        左连接查询：查询的结果为两个表匹配到的数据，左表特有的数据，对于右表中不存在的数据使用null填充

        select * from 表1 inner或left或right join 表2 on 表1.列 = 表2.列

子查询
    子查询：在一个 select 语句中,嵌入了另外一个 select 语句, 那么被嵌入的 select 语句称之为子查询语句
    主查询：主要查询的对象,第一条 select 语句
    主查询和子查询的关系：
        子查询是嵌入到主查询中
        子查询是辅助主查询的,要么充当条件,要么充当数据源
        子查询是可以独立存在的语句,是一条完整的 select 语句
    子查询分类：
        标量子查询: 子查询返回的结果是一个数据(一行一列)
            select * from students where age > (select avg(age) from students);
                查询班级学生平均年龄
                查询大于平均年龄的学生
        列子查询: 返回的结果是一列(一列多行)
            select name from classes where id in (select cls_id from students);
                找出学生表中所有的班级 id
                找出班级表中对应的名字
        行子查询: 返回的结果是一行(一行多列)
            select * from students where (height,age) = (select max(height),max(age) from students);
                查找班级年龄最大,身高最高的学生
"""


def main():
    pass


if __name__ == "__main__":
    main()
    






