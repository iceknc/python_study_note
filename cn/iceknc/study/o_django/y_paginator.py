# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/10
# @Desc  : 
'''
分页
    Django提供了数据分页的类，这些类被定义在django/core/paginator.py中。 类Paginator用于对列进行一页n条数据的分页运算。
    类Page用于表示第m页的数据。
    Paginator类实例对象
        方法_init_(列表,int)：返回分页对象，第一个参数为列表数据，第二个参数为每页数据的条数。
        属性count：返回对象总数。
        属性num_pages：返回页面总数。
        属性page_range：返回页码列表，从1开始，例如[1, 2, 3, 4]。
        方法page(m)：返回Page类实例对象，表示第m页的数据，下标以1开始。

    Page类实例对象
        调用Paginator对象的page()方法返回Page对象，不需要手动构造。
        属性object_list：返回当前页对象的列表。
        属性number：返回当前是第几页，从1开始。
        属性paginator：当前页对应的Paginator对象。
        方法has_next()：如果有下一页返回True。
        方法has_previous()：如果有上一页返回True。
        方法len()：返回当前页面对象的个数。

    示例：use_mysql/test_app/views.page
'''

def main():
    pass


if __name__ == "__main__":
    main()
    






