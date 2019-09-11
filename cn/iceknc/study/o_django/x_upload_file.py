# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/9
# @Desc  : 
"""
在Django中上传图片包括两种方式：
    在管理页面admin中上传图片
    自定义form表单中上传图片
上传图片后，将图片存储在服务器上，然后将图片的路径存储在表中。

创建包含图片的模型类
    将模型类的属性定义成models.ImageField类型。
        class Picture(models.Model):
            pic = models.ImageField(upload_to='<应用名>/')
打开<项目名>/settings.py文件，设置图片保存路径。因为图片也属于静态文件，所以保存到static目录下。
    MEDIA_ROOT=os.path.join(BASE_DIR,"static/media")
在static目录下创建media目录，再创建应用名称的目录

在管理页面admin中上传图片
    打开<应用名>/admin.py文件，注册Picture。

自定义form表单中上传图片
    打开<应用名>/views.py文件，创建视图pic_upload。
        def pic_upload(request):
            return render(request,'test_app/pic_upload.html')
    打开<应用名>/urls.py文件，配置url
         url(r'^pic_upload/$', views.pic_upload),
    打开<应用名>/views.py文件，创建视图pic_handle，用于接收表单保存图片。
        def pic_handle(request):
            f1=request.FILES.get('pic')
            fname='%s/booktest/%s'%(settings.MEDIA_ROOT,f1.name)
            with open(fname,'wb') as pic:
                for c in f1.chunks():
                    pic.write(c)
            return HttpResponse('OK')
    打开<应用名>/urls.py文件，配置url
        url(r'^pic_handle/$', views.pic_handle),

显示图片
    打开<应用名>/views.py文件，创建视图pic_show
        def pic_show(request):
            pic=Picture.objects.get(pk=1)
            context={'pic':pic}
            return render(request,'test_app/pic_show.html',context)
    打开<应用名>/urls.py文件，配置url
        url(r'^pic_show/$', views.pic_show),
"""


def main():
    pass


if __name__ == "__main__":
    main()
    






