# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/21
# @Desc  : 
from django.conf.urls import url
from test_app import views

urlpatterns = [
    url(r'^$', views.index),
    # 配置详细页url，\d+表示多个数字，小括号用于取值，建议复习下正则表达式
    url(r'^detail/(\d+)$', views.detail),
    url(r'^delete/(\d+)$', views.delete),
    url(r'^create/$', views.create),
]


def main():
    pass


if __name__ == "__main__":
    main()
