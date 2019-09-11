# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/6
# @Desc  : 
"""
静态文件
    项目中的CSS、图片、js都是静态文件。一般会将静态文件放到一个单独的目录中，以方便管理。在html页面中调用时，
    也需要指定静态文件的路径，Django中提供了一种解析的方式配置静态文件路径。静态文件可以放在项目根目录下，也可以放在应用的目录下，
    由于有些静态文件在项目中是通用的，所以推荐放在项目的根目录下，方便管理。
配置
    在<项目名>/settings.py文件中定义静态文件存放的物理目录。
        STATIC_URL = '/static/'
        STATICFILES_DIRS = [
            os.path.join(BASE_DIR, 'static'),
        ]
    Django提供了一种配置，可以在html页面中可以隐藏真实路径。
        STATIC_URL = '/<别名>/'
    为了安全可以通过配置项隐藏真实图片路径，在模板中写成固定路径，后期维护太麻烦，可以使用static标签，根据配置项生成静态文件路径。
        {%load static from staticfiles%}
        <img src="{%static "img/xxx.png" %}"/>
"""

def main():
    pass


if __name__ == "__main__":
    main()
    






