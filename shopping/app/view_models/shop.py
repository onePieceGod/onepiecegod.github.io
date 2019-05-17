# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 15:15
# @Author  : 张广东
# @Email   : 1536335429@qq.com
# @File    : shop.py
# @Software: PyCharm

class ShopViewModel():

    def __init__(self,shop):
        self.stockSize=shop['stockSize']    #存货量
        self.title=shop['title']
        self.price=shop['price']
        self.sellerScreenName=shop['sellerScreenName']              #卖家店铺
        self.brandName=shop['brandName']      #包括厂家名称
        self.keyValues=shop['keyValues']       #是一个列表里面包含字典键值对，有商品详细信息
        self.imageUrls=shop['imageUrls']       #是一组图片列表


'''
    @classmethod
    def package_collction(cls,data):
        returned={
            'data':[]
        }
        if data:
            returned['data']=cls.cut_shop_data(data)
        return returned



    @classmethod
    def cut_shop_data(cls,data):
        shops=[]
        for sh in data['data']:
            r={
                'stockSize':sh['stockSize'],
                'title':sh['title'],
                'price':sh['price'],
                'sellerScreenName':sh['sellerScreenName'],
                'brandName':sh['brandName'],
                'keyValues':sh['keyValues'],
                'imageUrls':sh['imageUrls']
            }
            shops.append(r)
        return shops
    '''
class Shopcollection():
    def __init__(self):
        self.shops=[]

    def fill(self,data):
        self.shops = [ShopViewModel(sh) for sh in data]
        return self.shops







