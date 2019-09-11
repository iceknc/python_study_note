# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/26
# @Desc  : 
"""
模型类关系
    关系字段类型
        关系型数据库的关系包括三种类型：
            ForeignKey：一对多，将字段定义在多的一端中。
            ManyToManyField：多对多，将字段定义在任意一端中。
            OneToOneField：一对一，将字段定义在任意一端中。
            可以维护递归的关联关系，使用'self'指定，详见"自关联"。
关联查询
    通过对象执行关联查询
        在定义模型类时，可以指定三种关联关系，最常用的是一对多关系，如本例中的"图书-英雄"就为一对多关系。
            由一到多的访问语法：
                一对应的模型类对象.多对应的模型类名小写_set  例：
                    b = BookInfo.objects.get(id=1)
                    b.heroinfo_set.all()
            由多到一的访问语法:
                多对应的模型类对象.多对应的模型类中的关系类属性名  例：
                    h = HeroInfo.objects.get(id=1)
                    h.hbook

            访问一对应的模型类关联对象的id语法:
                多对应的模型类对象.关联类属性_id  例：
                    h = HeroInfo.objects.get(id=1)
                    h.book_id
            查询编号为1的图书
                book=BookInfo.objects.get(pk=1)
            获得book图书的所有英雄
                book.heroinfo_set.all()
            获得编号为1的英雄
                hero=HeroInfo.objects.get(pk=1)
            获得hero英雄出自的图书
                hero.hbook

通过模型类执行关联查询
    由多模型类条件查询一模型类数据
        语法：关联模型类名小写__属性名__条件运算符=值
            如果没有"__运算符"部分，表示等于，结果和sql中的inner join相同
        查询图书，要求图书中英雄的描述包含'八'
            list = BookInfo.objects.filter(heroinfo__hcomment__contains='八')
    由一模型类条件查询多模型类数据
        语法：一模型类关联属性名__一模型类属性名__条件运算符=值
        查询书名为“天龙八部”的所有英雄
            list = HeroInfo.objects.filter(hbook__btitle='天龙八部')

自关联
    对于地区信息、分类信息等数据，表结构非常类似，每个表的数据量十分有限，为了充分利用数据表的大量数据存储功能，可以设计成一张表，
    内部的关系字段指向本表的主键，这就是自关联的表结构。
"""


def main():
    pass


if __name__ == "__main__":
    main()
