# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/23
# @Desc  : 
"""
字段查询
    实现sql中where的功能，调用过滤器filter()、exclude()、get()
    通过"属性名_id"表示外键对应对象的id值
    语法如下：
        属性名称和比较运算符间使用两个下划线，所以属性名不能包括多个下划线。
        属性名称__比较运算符=值

条件运算符
    查询等
        exact：表示判等
            查询编号为1的图书
                list=BookInfo.objects.filter(id__exact=1)
                list=BookInfo.objects.filter(id=1)
    模糊查询
        contains：是否包含(如果要包含%无需转义，直接写即可)
            查询书名包含'传'的图书
                list = BookInfo.objects.filter(btitle__contains='传')
        startswith、endswith：以指定值开头或结尾
            查询书名以'部'结尾的图书
                list = BookInfo.objects.filter(btitle__endswith='部')
    空查询
        isnull：是否为null
            查询书名不为空的图书
                list = BookInfo.objects.filter(btitle__isnull=False)
    范围查询
        in：是否包含在范围内
            查询编号为1或3或5的图书
                list = BookInfo.objects.filter(id__in=[1, 3, 5])
    比较查询
        gt、gte、lt、lte：大于、大于等于、小于、小于等于
            查询编号大于3的图书
                list = BookInfo.objects.filter(id__gt=3)
        不等于的运算符，使用exclude()过滤器
            查询编号不等于3的图书
                list = BookInfo.objects.exclude(id=3)
    日期查询
        year、month、day、week_day、hour、minute、second：对日期时间类型的属性进行运算
            查询1980年发表的图书
                list = BookInfo.objects.filter(bpub_date__year=1980)
            查询1980年1月1日后发表的图书
                list = BookInfo.objects.filter(bpub_date__gt=date(1990, 1, 1))
排序
    order by (查询所有的数据，all()可以省略)
        查询所有图书并按id从小到大排序
            list = BookInfo.objects.all().order_by('id')
        查询所有图书并按id从大到小排序
            list = BookInfo.objects.order_by('-id')
Q对象
    多个过滤器逐个调用表示逻辑与关系，同sql语句中where部分的and关键字
    如果需要实现逻辑或or的查询，需要使用Q()对象结合|运算符，Q对象被义在django.db.models中
    语法如下
        Q(属性名__运算符=值)
    查询阅读量大于20的图书，改写为Q对象如下
        list = BookInfo.objects.filter(Q(bread__gt=20))
    Q对象可以使用&、|连接，&表示逻辑与，|表示逻辑或
        查询阅读量大于20，或编号小于3的图书，只能使用Q对象实现
            list = BookInfo.objects.filter(Q(bread__gt=20) | Q(pk__lt=3))
    Q对象前可以使用~操作符，表示非not
        查询编号不等于3的图书
            list = BookInfo.objects.filter(~Q(pk=3))
F对象
    用于两个属性怎么比较呢
    定义在django.db.models中
    语法如下
        F(属性名)
    查询阅读量大于等于评论量的图书
        list = BookInfo.objects.filter(bread__gte=F('bcomment'))
    可以在F对象上使用算数运算
        查询阅读量大于2倍评论量的图书
            list = BookInfo.objects.filter(bread__gt=F('bcomment') * 2)
聚合函数
    使用aggregate()过滤器调用聚合函数。聚合函数包括：Avg，Count，Max，Min，Sum，被定义在django.db.models中。
        查询图书的总阅读量。
            list = BookInfo.objects.aggregate(Sum('bread'))
            注意aggregate的返回值是一个字典类型，格式如下：
                {'聚合类小写__属性名':值}
                如:{'sum__bread':3}
        使用count时一般不使用aggregate()过滤器。
            查询图书总数。
                list = BookInfo.objects.count()
                注意count函数的返回值是一个数字。

查询集
    查询集表示从数据库中获取的对象集合，在管理器上调用某些过滤器方法会返回查询集，查询集可以含有零个、一个或多个过滤器。
    过滤器基于所给的参数限制查询的结果，从Sql的角度，查询集和select语句等价，过滤器像where和limit子句

    返回查询集的过滤器如下：
        all()：返回所有数据。
        filter()：返回满足条件的数据。
        exclude()：返回满足条件之外的数据，相当于sql语句中where部分的not关键字。
        order_by()：对结果进行排序。
    返回单个值的过滤器如下：
        get()：返回单个满足条件的对象
            如果未找到会引发"模型类.DoesNotExist"异常。
            如果多条被返回，会引发"模型类.MultipleObjectsReturned"异常。
        count()：返回当前查询结果的总条数。
        aggregate()：聚合，返回一个字典。
    判断某一个查询集中是否有数据：
        exists()：判断查询集中是否有数据，如果有则返回True，没有则返回False

    两大特性
        惰性执行：创建查询集不会访问数据库，直到调用数据时，才会访问数据库，调用数据的情况包括迭代、序列化、与if合用。
        缓存：使用同一个查询集，第一次使用时会发生数据库的查询，然后把结果缓存下来，再次使用这个查询集时会使用缓存的数据。
    查询集的缓存
        每个查询集都包含一个缓存来最小化对数据库的访问。
        在新建的查询集中，缓存为空，首次对查询集求值时，会发生数据库查询，django会将查询的结果存在查询集的缓存中，并返回请求的结果，
        接下来对查询集求值将重用缓存中的结果
    限制查询集
        可以对查询集进行取下标或切片操作，等同于sql中的limit和offset子句。
            注意：不支持负数索引。
        对查询集进行切片后返回一个新的查询集，不会立即执行查询。
        如果获取一个对象，直接使用[0]，等同于[0:1].get()，但是如果没有数据，[0]引发IndexError异常，[0:1].get()如果没有数据
        引发DoesNotExist异常。
"""

def main():
    pass


if __name__ == "__main__":
    main()
    






