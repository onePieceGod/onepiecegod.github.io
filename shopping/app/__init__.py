# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 9:15
# @Author  : 张广东
# @Email   : 1536335429@qq.com
# @File    : __init__.py
# @Software: PyCharm
from flask import Flask
from app.models.base import db
from flask_login import LoginManager

login_manager=LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')

    register_blueprint(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view='web.login'



    with app.app_context():
        db.create_all()



    return app



def register_blueprint(app):
    from app.web.user import web
    from app.web.main import web
    app.register_blueprint(web)