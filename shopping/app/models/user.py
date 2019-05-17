# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 9:53
# @Author  : 张广东
# @Email   : 1536335429@qq.com
# @File    : user.py
# @Software: PyCharm

from app.models.shop import Shops,Bought
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer,String,Column
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.base import db
from flask_login import UserMixin
from app import login_manager


class User(db.Model,UserMixin):
    __tablename__='user'
    id = Column(Integer, primary_key=True,autoincrement=True)
    log_name=Column(String(30),unique=True,nullable=False)
    _password=Column(String(128),nullable=False)
    mail=Column(String(40),unique=True,nullable=False)
    money=Column(Integer,nullable=False,default=1000)
    shopid = relationship('Shops')
    boughtid=relationship('Bought')



    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,raw):
        self._password=generate_password_hash(raw)
        return self._password

    def check_password(self,pwd):
        return check_password_hash(self._password,pwd)




@login_manager.user_loader
def get_user(uid):
     return User.query.get(int(uid))


