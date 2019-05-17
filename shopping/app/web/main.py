# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 11:25
# @Author  : 张广东
# @Email   : 1536335429@qq.com
# @File    : main.py
# @Software: PyCharm4

from flask import render_template,request,jsonify,session,redirect,url_for,flash
from . import web
from app.forms.search import SearchForm
from spider.shop import Shop
from app.view_models.shop import ShopViewModel,Shopcollection
from app.models.base import db
from app.models.user import User
from app.models.shop import Shops,Bought
from datetime import datetime
from flask_login import login_required
from flask_login import current_user

@web.route('/index/',methods=['POST','GET'])
def index():
    return render_template('login.html')



@web.route('/shop/main',methods=['POST','GET'])
@login_required
def mains():
    name=current_user.log_name
    mon=current_user.money
    form=SearchForm()

    res=[]
    shop = Shop()
    res = shop.searchby_kw('小米')
    if form.validate_on_submit():
        kw=form.kw.data
        shop=Shop()
        res=shop.searchby_kw(kw)


    return render_template('index.html',res=res,form=form,name=name,mon=mon)


@web.route('/shop/buy',methods=['POST','GET'])
@login_required
def buy():
    st=request.args['st']
    p=request.args['price']
    t=request.args['title']
    img=request.args['img']
    pack = request.args['pack']
    brand = request.args['brand']
    url=request.args['url']


    money=current_user.money
    name=current_user.log_name
    f=float(p)
    if money >= f:
        q = money - f
        user.money = q
        db.session.commit()
        mon = current_user.money
        with db.auto_commit():
            bought=Bought()
            bought.uid=current_user.id
            bought.price = p
            bought.title = t
            bought.img = img
            bought.packInfo = pack
            bought.brandName = brand
            bought.url=url
            bought.datetime=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            db.session.add(bought)

    else:
        return redirect(url_for('web.chong',a=0))

    return render_template('buy.html',p=p,t=t,img=img,mon=mon,name=name,url=url)
@web.route('/shop/cauculate',methods=['POST','GET'])
def cauculate():
    p = request.args['price']
    email = session.get('mail')
    if email:
        user = User.query.filter_by(mail=email).first()
        money = user.money
        f=int(p)
        if money>=f:
            f=money-f
            with db.auto_commit():
                user.money=f
            mon=user.money
        else:
            flash('请充值')
    return redirect('buy.html',p=p,mon=mon)
@web.route('/user',methods=['POST','GET'])
@login_required
def user():
    user=current_user

    return render_template('user.html',user=user)


@web.route('/chong',methods=['POST','GET'])
@login_required
def chong():
    p = request.args['a']
    name=current_user.log_name


    money = current_user.money
    f = int(p)
    mon=f+money
    with db.auto_commit():
        current_user.money = mon
    mons = current_user.money
    flash('充值成功')

    return render_template('chongzhi.html',mon=mons,name=name)


@web.route('/shop/car',methods=['POST','GET'])
@login_required
def car():
    p = request.args['price']
    t = request.args['title']
    img = request.args['img']
    pack=request.args['pack']
    brand=request.args['brand']
    url=request.args['url']
    name=current_user.log_name

    mon = current_user.money
    id=current_user.id
    with db.auto_commit():
        shop=Shops()
        shop.uid=id
        shop.price=p
        shop.title=t
        shop.img=img
        shop.packInfo=pack
        shop.brandName=brand
        shop.url=url
        db.session.add(shop)
    s=Shops.query.order_by(-Shops.id).filter_by(uid=id).all()
    return render_template('car.html',s=s,mon=mon,name=name)



@web.route('/shop/bought',methods=['POST','GET'])
@login_required
def bought():

    name=current_user.log_name

    mon = current_user.money
    sp=Bought.query.order_by(-Bought.id).filter_by(uid=current_user.id).all()
    return render_template('bought.html',sp=sp,name=name,mon=mon)

@web.route('/shop/card',methods=['POST','GET'])
@login_required
def card():
    name=current_user.log_name

    mon = current_user.money
    s=Shops.query.order_by(-Shops.id).filter_by(uid=current_user.id).all()
    return render_template('car.html',s=s,mon=mon,name=name)

