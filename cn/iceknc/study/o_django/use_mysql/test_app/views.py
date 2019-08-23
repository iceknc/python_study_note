from django.shortcuts import render, redirect
from test_app.models import BookInfo, HeroInfo
from datetime import date


# Create your views here.
# 查询所有图书并显示
def index(request):
    list = BookInfo.objects.all()
    return render(request, 'test_app/index.html', {'title': '图书列表', 'list': list})


# 创建新图书
def create(request):
    book = BookInfo()
    book.btitle = '流星蝴蝶剑'
    book.bpub_date = date(1995, 12, 30)
    book.save()
    # 转向到首页
    return redirect('/')


# 逻辑删除指定编号的图书
def delete(request, id):
    book = BookInfo.objects.get(id=int(id))
    book.delete()
    # 转向到首页
    return redirect('/')


# 详细页，接收图书的编号，根据编号查询，再通过关系找到本图书的所有英雄并展示
def detail(request, bid):
    # 根据图书编号对应图书
    book = BookInfo.objects.get(id=int(bid))
    # 查找book图书中的所有英雄信息
    heros = book.heroinfo_set.all()
    # 将图书信息传递到模板中，然后渲染模板
    return render(request, 'test_app/detail.html', context={'book': book, 'heros': heros},
                  content_type='text/html; charset=utf-8')
