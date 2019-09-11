from django.db import models


# Create your models here.
class BookInfoManager(models.Manager):
    def all(self):
        return super().all().filter(isDelete=False)

    def create_book(self, title, pub_date):
        # 创建模型类对象self.model可以获得模型类
        book = self.model()
        book.btitle = title
        book.bpub_date = pub_date
        book.bread = 0
        book.bcommet = 0
        book.isDelete = False
        # 将数据插入进数据表
        book.save()
        return book


# 定义图书模型类BookInfo
class BookInfo(models.Model):
    objects = BookInfoManager()
    btitle = models.CharField(max_length=20, db_column='title')  # 图书名称
    bpub_date = models.DateField(db_column='pub_date')  # 发布日期
    bprice = models.DecimalField(db_column='price', max_digits=10, decimal_places=2, default=0.00)  # 价格
    bread = models.IntegerField(default=0, db_column='read')  # 阅读量
    bcomment = models.IntegerField(default=0, db_column='comment')  # 评论量
    isDelete = models.BooleanField(default=False)  # 逻辑删除

    def __str__(self):
        return self.btitle


# 定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20, db_column='name')  # 英雄姓名
    hgender = models.BooleanField(default=True, db_column='gender')  # 英雄性别
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    hcomment = models.CharField(max_length=200, db_column='comment', null=True,
                                blank=False)  # 英雄描述信息 对应的数据库中的字段可以为空，但通过后台管理页面添加英雄信息时hcomment对应的输入框不能为空
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)  # 英雄与图书表的关系为一对多，所以属性定义在英雄模型类中


class AreaInfo(models.Model):
    atitle = models.CharField(max_length=50, db_column='title')
    aparent = models.ForeignKey('self', null=True, blank=True, db_column='parent_id', on_delete=models.CASCADE)


class ChinaRegion(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    parentCode = models.CharField(max_length=50, null=True)
    parentId = models.ForeignKey('self', db_column='parentId', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'china_region'

    def parentName(self):
        if self.parentId is None:
            return ''
        else:
            return self.parentId.name

    parentName.short_description = '父区域名称'


class Picture(models.Model):
    pic = models.ImageField(upload_to='test_app/')

from tinymce.models import HTMLField
class GoodsInfo(models.Model):
    content = HTMLField()
