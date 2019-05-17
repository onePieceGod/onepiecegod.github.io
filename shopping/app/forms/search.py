# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 16:09
# @Author  : 张广东
# @Email   : 1536335429@qq.com
# @File    : search.py
# @Software: PyCharm
from wtforms import Form,StringField,IntegerField,SubmitField
from wtforms.validators import Length,NumberRange,DataRequired
from flask_wtf import FlaskForm
class SearchForm(FlaskForm):
    kw=StringField(validators=[Length(1,30),DataRequired()],default='小米')
    submit=SubmitField('搜索商品')