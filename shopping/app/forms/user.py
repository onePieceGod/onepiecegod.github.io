# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 10:02
# @Author  : 张广东
# @Email   : 1536335429@qq.com
# @File    : user.py
# @Software: PyCharm

from wtforms import Form, StringField, IntegerField, PasswordField,SubmitField,TextField
from wtforms.validators import EqualTo, Length, NumberRange, DataRequired, Email, \
    ValidationError
from app.models.user import User
from flask_wtf import FlaskForm
'''
class RegisterForm(FlaskForm):
    log_name=StringField('登录名',validators=[Length(1,30),DataRequired()])
    name=StringField('姓名',validators=[Length(1,30),DataRequired()])
    password=PasswordField('密码',validators=[Length(3,30),DataRequired()])
    password_again=PasswordField('确认密码',validators=[Length(3,30),EqualTo('password','两次密码不一致'),DataRequired()])
    mail=TextField('邮箱',validators=[Email(message='您输入的邮箱格式不正确')])
    telephone=StringField('电话',validators=[Length(7,15)])
    submit=SubmitField('注册')

    def validate_email(self, field):
        # db.session.
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已存在')

class LoginForm(FlaskForm):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮箱不符合规范')])
    password = PasswordField(validators=[
        DataRequired(message='密码不可以为空，请输入你的密码'), Length(6, 32)])
    submit=SubmitField('登录')


class EmailForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮箱不符合规范')])


class ResetPasswordForm(Form):
    password1 = PasswordField(validators=[
        DataRequired(),
        Length(6, 32, message='密码长度至少需要在6到32个字符之间'),
        EqualTo('password2', message='两次输入的密码不相同')])
    password2 = PasswordField(validators=[
        DataRequired(), Length(6, 32)])
'''

from flask_wtf import FlaskForm
from wtforms.fields import SubmitField,StringField,PasswordField,TextField
from wtforms.validators import EqualTo,DataRequired,Length,Email

class Register(FlaskForm):
    log_name=StringField('登录名',validators=[Length(1,30),DataRequired()])
    password=PasswordField('密码',validators=[Length(3,30),DataRequired()])
    password_again=PasswordField('确认密码',validators=[Length(3,30),EqualTo('password','两次密码不一致'),DataRequired()])
    mail=StringField('邮箱',validators=[Email(message='您输入的邮箱格式不正确')])
    submit=SubmitField('注册')

    def validate_mail(self, field):
        # db.session.
        if User.query.filter_by(mail=field).first():
            a='电子邮件已被注册'
            return a

    def validate_log_name(self, field):
        if User.query.filter_by(log_name=field).first():
            a='昵称已存在'
            return a

class Login(FlaskForm):
    mail=StringField('邮箱',validators=[Length(5,30),DataRequired()])
    password=PasswordField('密码',validators=[Length(3,30),DataRequired()])
    submit=SubmitField('登录')