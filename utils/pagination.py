#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
-----------------------------------------------------------
    @FileName  :pagination.py
    @Time      :2023/2/22 21:27
    @Author    :LittleSeven
    @Address   ：https://gitee.com/linguchong/Demo1_1.git
-----------------------------------------------------------
'''
from rest_framework.pagination import PageNumberPagination as _PageNumberPagination
from rest_framework.response import Response


class PageNumberPagination(_PageNumberPagination):
    # 指定默认每一页3条数据
    page_size = 3
    # 指定前端用于指定页码的查询字符串参数名称
    page_query_param = 'pp'
    # 指定前端用于指定页码的查询字符串参数描述
    page_query_description = '获取的页码'
    # 指定前端用于每一页显示的数据条数的查询字符串参数描述
    page_size_query_param = 'ss'
    page_size_query_description = '每一页数据条目数'
    # 指定前端最大条目数，
    max_page_size = 50

    invalid_page_message = '无效页码'

    def get_paginated_response(self, data):
        response = super().get_paginated_response(data)
        response.data['max_num'] = self.page.paginator.num_pages
        response.data['current_num'] = self.page.number
        return response