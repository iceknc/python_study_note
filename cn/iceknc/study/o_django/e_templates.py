# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/21
# @Desc  : 
"""
模板
    创建模板
        为应用first_app下的视图index创建模板index.html
        设置查找模板的路径：打开hello_django/settings.py文件，设置TEMPLATES的DIRS值
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
        定义模板
            在模板中输出变量语法如下，变量可能是从视图中传递过来的，也可能是在模板中定义的
                {{变量名}}
            在模板中编写代码段语法如下
                {%代码段%}
        视图调用模板
            调用模板分为三步骤：
                1.找到模板
                2.定义上下文
                3.渲染模板
            打开first_app/views.py文件，调用上面定义的模板文件
                from django.http import HttpResponse
                from django.template import loader,RequestContext

                def index(request):
                    # 1.获取模板
                    template=loader.get_template('test_app/index.html')
                    # 2.定义上下文
                    context = {'title': '图书列表', 'list': range(10)}
                    # 3.渲染模板
                    return HttpResponse(template.render(context=context, request=request))
        视图调用模板简写
            from django.shortcuts import render

            def index(request):
                context={'title':'图书列表','list':range(10)}
                return render(request,'test_app/index.html',context=context, content_type='text/html; charset=utf-8')

"""


def main():
    pass


if __name__ == "__main__":
    main()
