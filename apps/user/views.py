import hashlib
import time

from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

from apps.user.models import User
from exts import db

user_bp1 = Blueprint('user1', __name__, url_prefix='/user')

required_list = ['/user/center']

@user_bp1.before_app_request
def before_request():
    if request.path in required_list:
        if session['uid']:
            user = User.query.get(session['uid'])
            if user.role == 'supplier':
               return render_template('user/message.html')
                # return redirect(url_for('user1.index'))

        else:
            return redirect(url_for('login.index'))



@user_bp1.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        email = request.form.get('email')
        if password == repassword:
            user = User()
            user.username = username
            user.password = generate_password_hash(password)
            user.phone = phone
            user.email = email
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user1.index'))
        else:
            return '密码输入不一致！'
    else:
        return render_template('user/register.html')


@user_bp1.route('/checkphone')
def check_phone():
    phone = request.args.get('phone')

    if User.query.filter(phone == User.phone).all():
        return jsonify(code=400, msg='此号码已被注册')
    else:
        return jsonify(code=200, msg='此号码可以注册')


@user_bp1.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        users = User.query.filter(User.username == username).all()
        for user in users:
            flag = check_password_hash(user.password,password)
            print(user.password,password)
            print(flag)
            if flag:
                # response = redirect(url_for('user1.index'))
                # response.set_cookie('uid',str(user.id),max_age=1800)
                # return response
                session['uid'] = user.id
                return redirect(url_for('user1.index'))
        return render_template('user/login.html',msg='用户名或密码输入不正确')
    if request.method == 'GET':
        return render_template('user/login.html')


@user_bp1.route('/')
def index():
    # uid = request.cookies.get('uid',None)
    uid = session.get('uid')
    if uid :
        user = User.query.get(uid)
        print(user.role)

        return render_template('user/index.html',user=user)
    else:
        return render_template('user/index.html')

@user_bp1.route('/logout')
def logout():
    # response = redirect(url_for('user1.index'))
    # response.delete_cookie('uid')
    session.clear()
    return redirect(url_for('user1.index'))

@user_bp1.route('/center')
def center():
    uid = session.get('uid')
    if uid:
        user = User.query.get(uid)

        return render_template('user/center.html', user=user)
    else:
        return render_template('user/center.html')

