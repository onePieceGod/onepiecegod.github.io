# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 16:02
# @Author  : 张广东
# @Email   : 1536335429@qq.com
# @File    : httper.py
# @Software: PyCharm
import requests


class HTTP:
    # 经典类和新式类
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url, headers={"Accept-Encoding": "gzip",'Connection':'close'})
        # restful
        # json
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text