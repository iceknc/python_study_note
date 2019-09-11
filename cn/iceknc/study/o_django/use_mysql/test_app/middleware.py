# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/6
# @Desc  : 
from django.utils.deprecation import MiddlewareMixin

class MyMiddle(MiddlewareMixin):
    def __init__(self, get_response):
        print('--------------init')
        super().__init__(get_response)

    def process_request(self, request):
        print('--------------request')

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        print('--------------view')

    def process_response(self, request, response):
        print('--------------response')
        return response
