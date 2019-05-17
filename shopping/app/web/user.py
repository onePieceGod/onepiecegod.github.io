# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 10:05
# @Author  : 张广东
# @Email   : 1536335429@qq.com
# @File    : user.py
# @Software: PyCharm
from . import web
from flask import render_template, request, redirect, url_for, flash,session
from flask_login import login_user, logout_user, current_user, login_required
from app.models.user import User
from app.models.base import db
from app.forms.user import Register,Login
from flask_login import login_required,login_user


@web.route('/register/',methods=['GET','POST'])
def register():
    form=Register()
    if form.validate():
        log_name=form.log_name.data
        flash(form.validate_log_name(log_name))
        password=form.password.data
        password_again=form.password_again.data
        mail=form.mail.data
        flash(form.validate_mail(mail))
        with db.auto_commit():
            user=User()
            user.log_name=log_name
            user.password=password_again
            user.mail=mail
            db.session.add(user)
        return redirect(url_for('web.login'))
    else:
        flash('注册失败')
    return render_template('register.html',form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(mail=form.mail.data).first()
        print(user.password)
        if user and user.check_password(form.password.data):
            login_user(user,remember=True)
            # session['mail']=form.mail.data
            # session['password']=form.password.data
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                next = url_for('web.mains')
            return redirect(next)
        else:
            print('sadasdas')
            flash('账号不存在或密码错误')
    else:
        flash('登录失败')
    return render_template('login.html', form=form)

@web.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('web.index'))

