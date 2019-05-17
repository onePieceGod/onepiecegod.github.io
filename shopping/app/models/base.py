# -*- coding: utf-8 -*-
# @Time    : 2018/10/1 16:25
# @Author  : 张广东
# @Email   : 1536335429@qq.com
# @File    : base.py
# @Software: PyCharm

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from contextlib import contextmanager

class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e



db=SQLAlchemy()