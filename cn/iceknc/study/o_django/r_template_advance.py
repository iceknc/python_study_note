# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/4
# @Desc  : 
"""
模板
    作为Web框架，Django提供了模板，用于编写html代码，还可以嵌入模板代码更快更方便的完成页面开发，再通过在视图中渲染模板，
    将生成最终的html字符串返回给客户端浏览器。模版致力于表达外观，而不是程序逻辑。模板的设计实现了业务逻辑view与显示内容
    template的分离，一个视图可以使用任意一个模板，一个模板可以供多个视图使用
    模板包含两部分：
        静态部分，包含html、css、js。
        动态部分，就是模板语言。
模板语言
    模板语言包括4种类型，分别是：
        变量 : 变量名必须由字母、数字、下划线（不能以下划线开头）和点组成。
            语法 : {{变量}}
            当模版引擎遇到点如book.title，会按照下列顺序解析：
                1.字典book['title']
                2.先属性后方法，将book当作对象，查找属性title，如果没有再查找方法title()
                3.如果是格式为book.0则解析为列表book[0]
                    如果变量不存在则插入空字符串''。
            在模板中调用方法时不能传递参数。
        标签
            语法 : {%代码段%}
            for标签语法如下：
                {%for item in 列表%}
                    循环逻辑
                {{forloop.counter}}表示当前是第几次循环，从1开始
                {%empty%}
                列表为空或不存在时执行此逻辑
                {%endfor%}
            if标签语法如下：
                {%if ...%}
                    逻辑1
                {%elif ...%}
                    逻辑2
                {%else%}
                    逻辑3
                {%endif%}
            比较运算符如下：
                注意：运算符左右两侧不能紧挨变量或常量，必须有空格。
                ==    !=    <   >   <=  >=
            布尔运算符如下：
                and    or   not
        过滤器
            语法如下:
                变量|过滤器:参数
                使用管道符号|来应用过滤器，用于进行计算、转换操作，可以使用在变量、标签中。
                如果过滤器需要参数，则使用冒号:传递参数。
                长度length，返回字符串包含字符的个数，或列表、元组、字典的元素个数。
                默认值default，如果变量不存在时则返回默认值。
                    data|default:'默认值'
                日期date，用于对日期类型的值进行字符串格式化，常用的格式化字符如下：
                    Y表示年，格式为4位，y表示两位的年  m表示月，格式为01,02,12等。
                    d表示日, 格式为01,02等    j表示日，格式为1,2等。
                    H表示时，24进制，h表示12进制的时。
                    i表示分，为0-59    s表示秒，为0-59。
                    value|date:"Y年m月j日  H时i分s秒"
        注释
            在模板中使用如下模板注释，这段代码不会被编译，不会输出到客户端；html注释只能注释html内容，不能注释模板语言。
            单行注释语法如下：
                {#...#}
            注释可以包含任何模版代码，有效的或者无效的都可以。
                {# { % if foo % }bar{ % else % } #}
            多行注释使用comment标签，语法如下：
                {%comment%}
                ...
                {%endcomment%}
自定义过滤器
    过滤器就是python中的函数，注册后就可以在模板中当作过滤器使用，下面以求余为例开发一个自定义过滤器mod。
    1.在应用中创建templatetags目录，创建_init_文件，内容为空。
    2.在"<应用>/templatetags"目录下创建filters.py文件，代码如下：
        #导入Library类
        from django.template import Library

        #创建一个Library类对象
        register=Library()

        #使用装饰器进行注册
        @register.filter
        #定义求余函数mod，将value对2求余
        def mod(value):
            return value%2 == 0
    3.使用时要先导入
        {%load filters%}

    示例 <use_mysql>/<test_app>
模板继承
    模板继承和类的继承含义是一样的，主要是为了提高代码重用，减轻开发人员的工作量。典型应用：网站的头部、尾部信息

    父模板
        如果发现在多个模板中某些内容相同，那就应该把这段内容定义到父模板中。
        标签block：用于在父模板中预留区域，留给子模板填充差异性的内容，名字不能相同。
        为了更好的可读性，建议给endblock标签写上名字，这个名字与对应的block名字相同。父模板中也可以使用上下文中传递过来的数据。
            {%block 名称%}
                预留区域，可以编写默认内容，也可以没有默认内容
            {%endblock  名称%}
    子模板
        标签extends：继承，写在子模板文件的第一行。
            {% extends "父模板路径"%}
        子模版不用填充父模版中的所有预留区域，如果子模版没有填充，则使用父模版定义的默认值。
        填充父模板中指定名称的预留区域。
            {%block 名称%}
                实际填充内容
            {{block.super}}用于获取父模板中block的内容
            {%endblock 名称%}
    示例 <use_mysql>/<test_app>.views.temp_inherit

HTML转义
    模板对上下文传递的字符串进行输出时，会对以下字符自动转义。
        小于号< 转换为 &lt;
        大于号> 转换为 &gt;
        单引号' 转换为 &#39;
        双引号" 转换为 &quot;
        与符号& 转换为 &amp;
    示例 <use_mysql>/<test_app>.views.html_escape

    关闭转义
        过滤器escape可以实现对变量的html转义，默认模板就会转义，一般省略。
            {{t1|escape}}
        过滤器safe：禁用转义，告诉模板这个变量是安全的，可以解释执行。
            {{data|safe}}
        标签autoescape：设置一段代码都禁用转义，接受on、off参数。
            {%autoescape off%}
                ...
            {%endautoescape%}
    字符串字面值
        对于在模板中硬编码的html字符串，不会转义。如果希望出现转义的效果，则需要手动编码转义

"""

def main():
    pass


if __name__ == "__main__":
    main()
    






