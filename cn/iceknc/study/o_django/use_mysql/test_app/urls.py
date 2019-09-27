# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/21
# @Desc  : 
from django.conf.urls import url
from test_app import views

app_name = '[test_app]'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # 配置详细页url，\d+表示多个数字，小括号用于取值，建议复习下正则表达式
    url(r'^detail/(\d+)$', views.detail),
    url(r'^delete/(\d+)$', views.delete),
    url(r'^create/$', views.create),
    url(r'^area$', views.area_province, name='area'),
    url(r'^area_advance$', views.area),
    url(r'^area/(\d+)$', views.area_province_city, name='province_city'),
    url(r'^area/(?P<pid>\d+)/(?P<cid>\d+)$', views.area_province_city_county, name='province_city_county'),
    url(r'^showReqArg/$', views.show_req_arg),
    url(r'^showReqDoor/$', views.show_req_door),
    url(r'^json/$', views.json),
    url(r'^json/get/$', views.json_get),
    url(r'^redirect/$', views.redirect),
    url(r'^cookieSet/$', views.cookie_set),
    url(r'^cookieGet/$', views.cookie_get),
    url(r'^session/$', views.session_set),
    url(r'^tempInherit/$', views.temp_inherit),
    url(r'^escape/$', views.html_escape),
    url(r'^login/$', views.login),
    url(r'^login_check/$', views.login_check),
    url(r'^post/$', views.post),
    url(r'^post_action/$', views.post_action),
    url(r'^verify_code/$', views.verify_code),
    url(r'^verify_code/(\d+)$', views.verify_code_copy),
    url(r'^verify_show/$', views.verify_show),
    url(r'^verify_yz/$', views.verify_yz),
    url(r'^url_reverse/$', views.url_reverse),
    url(r'^code_reverse/$', views.code_reverse),
    url(r'^pic_upload/$', views.pic_upload),
    url(r'^pic_handle/$', views.pic_handle),
    url(r'^pic_show/$', views.pic_show),
    url(r'^page/(?P<pIndex>[0-9]*)/$', views.page),
    url(r'^province_json/$', views.province_json),
    url(r'^area_json/(\d+)/$', views.area_json),
    url(r'^edit/$', views.edit),
    url(r'^show/', views.show),
    url(r'^query/', views.query),
    url(r'^session_set/$',views.session_set),
    url(r'^session_get/$', views.session_get),
]


def main():
    pass


if __name__ == "__main__":
    main()
