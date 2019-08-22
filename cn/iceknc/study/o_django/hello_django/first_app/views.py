from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from first_app.models import BookInfo, HeroInfo


# Create your views here.

def index(request):
    # template = loader.get_template("first_app/index.html")
    # context = {'title': '图书列表', 'list': range(10)}
    # return HttpResponse(template.render(context=context, request=request))
    # return render(request, 'first_app/index.html', context={'title': '图书列表', 'list': range(10)}, content_type='text/html; charset=utf-8')

    # 查询所有图书
    booklist = BookInfo.objects.all()
    # 将图书列表传递到模板中，然后渲染模板
    return render(request, 'first_app/index.html', context={'title': '图书列表', 'booklist': booklist},
                  content_type='text/html; charset=utf-8')


# 详细页，接收图书的编号，根据编号查询，再通过关系找到本图书的所有英雄并展示
def detail(request, bid):
    # 根据图书编号对应图书
    book = BookInfo.objects.get(id=int(bid))
    # 查找book图书中的所有英雄信息
    heros = book.heroinfo_set.all()
    # 将图书信息传递到模板中，然后渲染模板
    return render(request, 'first_app/detail.html', context={'book': book, 'heros': heros},
                  content_type='text/html; charset=utf-8')


def home(request):
    return HttpResponse('home page')
