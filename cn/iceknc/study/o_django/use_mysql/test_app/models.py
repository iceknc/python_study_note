from django.db import models


# Create your models here.

# 定义图书模型类BookInfo
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, db_column='title')  # 图书名称
    bpub_date = models.DateField(db_column='pub_date')  # 发布日期
    bprice = models.DecimalField(db_column='price', max_digits=10, decimal_places=2,default=0.00)  # 价格
    bread = models.IntegerField(default=0, db_column='read')  # 阅读量
    bcomment = models.IntegerField(default=0, db_column='comment')  # 评论量
    isDelete = models.BooleanField(default=False)  # 逻辑删除


# 定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20, db_column='name')  # 英雄姓名
    hgender = models.BooleanField(default=True, db_column='gender')  # 英雄性别
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    hcomment = models.CharField(max_length=200, db_column='comment', null=True,
                                blank=False)  # 英雄描述信息 对应的数据库中的字段可以为空，但通过后台管理页面添加英雄信息时hcomment对应的输入框不能为空
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)  # 英雄与图书表的关系为一对多，所以属性定义在英雄模型类中
