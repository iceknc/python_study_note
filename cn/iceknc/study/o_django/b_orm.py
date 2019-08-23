# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/15
# @Desc  : 
"""
ORM框架
    O是object，也就类对象的意思，R是relation，翻译成中文是关系，也就是关系数据库中数据表的意思，M是mapping，是映射的意思。
    在ORM框架中，它帮我们把类和数据表进行了一个映射，可以让我们通过类和类对象就能操作它所对应的表格中的数据。ORM框架还有一个功能，
    它可以根据我们设计的类自动帮我们生成数据库中的表格，省去了我们自己建表的过程。

    django中内嵌了ORM框架，不需要直接面向数据库编程，而是定义模型类，通过模型类和对象完成数据表的增删改查操作。

    使用django进行数据库开发的步骤如下：
        1.在models.py中定义模型类
            模型类定义在models.py文件中，继承自models.Model类。(不需要定义主键列，在生成时会自动添加，并且值为自动增长。)
        2.迁移
            生成迁移文件：根据模型类生成创建表的迁移文件
                python manage.py makemigrations
            执行迁移：根据第一步生成的迁移文件在数据库中创建表
                python manage.py migrate
                    数据表的默认名称为: <app_name>_<model_name>
        3.通过类和对象完成数据增删改查操作
            进入项目shell
                python manage.py shell
            导入相关的models
                from test_app.models import BookInfo, HeroInfo
            查询所有图书信息
                BookInfo.objects.all()
                BookInfo.objects.get(id=1)
            新建图书对象
                b=BookInfo()
                b.btitle="射雕英雄传"
                from datetime import date
                b.bpub_date=date(1991,1,31)
                b.save()
            修改图书信息
                b.bpub_date=date(2017,1,1)
                b.save()
            删除图书信息
                b.delete()

            对象的关联操作
                创建一个BookInfo对象
                    b=BookInfo()
                    b.btitle='abc'
                    b.bpub_date=date(2017,1,1)
                    b.save()
                创建一个HeroInfo对象
                    h=HeroInfo()
                    h.hname='a1'
                    h.hgender=False
                    h.hcomment='he is a boy'
                    h.hbook=b
                    h.save()
                图书与英雄是一对多的关系，django中提供了关联的操作方式。

                获得关联集合：返回当前book对象的所有hero。
                    b.heroinfo_set.all()
"""

def main():
    pass


if __name__ == "__main__":
    main()
    






