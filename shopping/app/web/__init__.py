# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 9:16
# @Author  : 张广东
# @Email   : 1536335429@qq.com
# @File    : __init__.py
# @Software: PyCharm
from flask import Blueprint
web = Blueprint('web', __name__)
from app.web import user
from app.web import main