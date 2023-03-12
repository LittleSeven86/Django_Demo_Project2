#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
-----------------------------------------------------------
    @FileName  :test.py
    @Time      :2023/3/12 20:02
    @Author    :LittleSeven
    @Address   ：https://gitee.com/linguchong/Django_Project_Demo.git
-----------------------------------------------------------
'''
from httprunner import HttpRunner

httprun = HttpRunner()
httprun.runpath('/Users/z.m/pythonProject/Demo_one/demo/testcases/login_demo.yml')

