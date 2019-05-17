# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 10:31
# @Author  : 张广东
# @Email   : 1536335429@qq.com
# @File    : shop.py
# @Software: PyCharm

# coding:utf-8
"""
Compatible for python2.x and python3.x
requirement: pip install requests
"""

#coding:utf-8

from __future__ import print_function
import requests
from app.lib.httper import HTTP
class Shop():
# 请求示例 url 默认请求参数已经做URL编码
    url = "http://api01.bitspaceman.com:8000/product/gome?kw={}&apikey=00qeyC0Oo6qcxxA0LJwwNt8aTGbm6oS9RCOAmGgeAXOs3wvRCFt9SrRyv5oXgpHc&pageToken=1"


    def __init__(self):
        self.data=[]



    def searchby_kw(self,kw):
        url=self.url.format(kw)
        print(url)
        result=HTTP.get(url)
        print(type(result))
        self.data=result['data']
        return self.data



