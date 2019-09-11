from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect as red
from test_app.models import BookInfo, HeroInfo, AreaInfo, ChinaRegion, Picture, GoodsInfo
from datetime import date
from django.http import JsonResponse, HttpResponseRedirect
from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator


# Create your views here.
# 查询所有图书并显示
def index(request):
    print('============index============')
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


def area_province(request):
    province = ChinaRegion.objects.filter(parentCode=None)
    print(province)
    return render(request, 'test_app/province.html', context={'list': province})


def area_province_city(request, pid):
    province_name = ChinaRegion.objects.get(code=pid).name
    city_list = ChinaRegion.objects.filter(parentCode=pid)
    return render(request, 'test_app/province_city.html',
                  context={'list': city_list, 'pname': province_name, 'pid': pid})


def area_province_city_county(request, pid, cid):
    province_name = ChinaRegion.objects.get(code=pid).name
    city_name = ChinaRegion.objects.get(code=cid).name
    region_list = ChinaRegion.objects.filter(parentCode=cid)
    return render(request, 'test_app/province_city_county.html',
                  context={'list': region_list, 'pname': province_name, 'cname': city_name, 'pid': pid})


def show_req_door(request):
    return render(request, 'test_app/show_req_door.html')


def show_req_arg(request):
    if request.method == 'GET':
        a = request.GET.get('a')
        b = request.GET.get('b')
        c = request.GET.get('c')
        return render(request, 'test_app/show_get_arg.html', context={'a': a, 'b': b, 'c': c})
    else:
        name = request.POST.get('user_name')
        gender = request.POST.get('gender')
        hobby = request.POST.getlist('hobby')
        return render(request, 'test_app/show_post_arg.html', context={'name': name, 'gender': gender, 'hobbys': hobby})


def json(request):
    return render(request, 'test_app/json.html')


def json_get(request):
    return JsonResponse({'h1': 'hello', 'h2': 'world'})


def redirect(request):
    # return HttpResponseRedirect('/')
    return red('/')


def cookie_set(request):
    response = HttpResponse("<h1>设置Cookie，请查看响应报文头</h1>".encode('utf-8'))
    response.set_cookie('h1', bytes('你好cookie', 'utf8').decode('ISO-8859-1'))
    return response


def cookie_get(request):
    response = HttpResponse("读取Cookie，数据如下：<br>")
    if 'h1' in request.COOKIES:
        response.write('<h1>' + request.COOKIES['h1'].encode("iso-8859-1").decode('utf8') + '</h1>')
    return response


def session_set(request):
    # request.session['session_key'] = 'session_value'
    # return HttpResponse('写session')
    session_value = request.session.get('session_key')
    return HttpResponse(session_value)


def temp_inherit(request):
    context = {'title': '模板继承', 'list': BookInfo.objects.all()}
    return render(request, 'test_app/temp_inherit.html', context)


def html_escape(request):
    context = {'content': '<h1>hello world</h1>'}
    return render(request, 'test_app/html_escape.html', context=context)


def login(request):
    return render(request, 'test_app/login.html')


def login_check(request):
    username = request.POST.get('username')  # 获取用户名
    password = request.POST.get('password')  # 获取密码
    # 校验
    if username == 'admin' and password == '123':
        request.session['username'] = username  # 记住登录用户名
        request.session['islogin'] = True  # 判断用户是否已登录
        return red('/post/')
    else:
        return red('/login/')


def post(request):
    return render(request, 'test_app/post.html')


def post_action(request):
    if request.session['islogin']:
        username = request.session['username']
        return HttpResponse('用户' + username + '发了一篇帖子')
    else:
        return HttpResponse('发帖失败')


def verify_code_copy(request, temp):
    return verify_code(request)


def verify_code(request):
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 30
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    print(rand_str)
    font = ImageFont.truetype("C:\Windows\Fonts\simsunb.ttf", 23)
    # font = ImageFont.load("C:\Windows\Fonts\Adobe Arabic")
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 1), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 1), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 1), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 1), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


def verify_show(request):
    return render(request, 'test_app/verify_show.html')


def verify_yz(request):
    yzm = request.POST.get('yzm')
    verifycode = request.session['verifycode']
    response = HttpResponse('no')
    if yzm == verifycode:
        response = HttpResponse('ok')
    return response


def url_reverse(request):
    return render(request, "test_app/url_reverse.html")


def code_reverse(request):
    # url = reverse('test_app:area')
    # url = reverse('test_app:province_city', args=(44,))
    url = reverse('test_app:province_city_county', kwargs={'pid': 44, 'cid': 4402})
    return red(url)


def pic_upload(request):
    return render(request, 'test_app/pic_upload.html')


def pic_handle(request):
    f1 = request.FILES.get('pic')
    fname = '%s/test_app/%s' % (settings.MEDIA_ROOT, f1.name)
    with open(fname, 'wb') as pic:
        for c in f1.chunks():
            pic.write(c)
    return HttpResponse('OK')


def pic_show(request):
    pic = Picture.objects.get(pk=1)
    context = {'pic': pic}
    return render(request, 'test_app/pic_show.html', context)


def page(request, pIndex):
    all = ChinaRegion.objects.all()
    paginator = Paginator(all, 50)
    # 如果当前没有传递页码信息，则认为是第一页，这样写是为了请求第一页时可以不写页码
    if pIndex == '':
        pIndex = '1'
        # 通过url匹配的参数都是字符串类型，转换成int类型
    pIndex = int(pIndex)
    # 获取第pIndex页的数据
    result = paginator.page(pIndex)
    # 获取所有的页码信息
    plist = paginator.page_range
    # 将当前页码、当前页的数据、页码信息传递到模板中
    return render(request, 'test_app/page_test.html', {'list': result, 'plist': plist, 'pIndex': pIndex})


def area(request):
    return render(request, 'test_app/area_advance.html')


def province_json(request):
    province = ChinaRegion.objects.filter(parentCode=None)
    result = []
    for pro in province:
        result.append([pro.code, pro.name])
    return JsonResponse({'data': result})

def area_json(request, pCode):
    city = ChinaRegion.objects.filter(parentCode=pCode)
    result = []
    for c in city:
        result.append([c.code, c.name])
    return JsonResponse({'data': result})

def edit(request):
    return render(request,'test_app/editor.html')

def show(request):
    goods=GoodsInfo.objects.get(pk=1)
    context={'g':goods}
    return render(request,'test_app/show.html',context)

def query(request):
    return render(request,'test_app/query.html')