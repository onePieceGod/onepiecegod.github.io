# -*- coding: utf-8 -*-
# @Time    : 2018/9/28 21:47
# @Author  : 张广东
# @Email   : 1536335429@qq.com
# @File    : shop.py
# @Software: PyCharm

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer,String,Column,Float,DATETIME,SmallInteger,ForeignKey
from app.models.base import db
from sqlalchemy.orm import relationship


class Shops(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title=Column(String(100))
    price=Column(Float)
    packInfo=Column(String(100))
    brandName=Column(String(100))
    img=Column(String(100))
    url=Column(String(100))
    state = Column(SmallInteger, default=1)
    uid=Column(Integer,ForeignKey('user.id'))

class Bought(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100))
    price = Column(Float)
    packInfo = Column(String(100))
    brandName = Column(String(100))
    img = Column(String(100))
    url = Column(String(100))
    datetime=Column(DATETIME,nullable=False)
    state=Column(SmallInteger,default=1)
    uid = Column(Integer, ForeignKey('user.id'))

