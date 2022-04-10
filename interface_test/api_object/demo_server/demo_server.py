#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2021/10/28 14:46
# @Author:ytq
# @File:demo_server.py
import functools
import re

from flask import request, jsonify, Flask
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import Serializer

app = Flask(__name__)
SECRET_KEY = "ahsj$#^skjdkjjjk"

username = "root"
pwd = "123456"
ip = "47.92.149.0"
port = "3366"
database = "test_db"
# 设置mysql 链接方法是
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}?charset=utf8'
# 解决warning问题
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 数据库与flask应用绑定
db = SQLAlchemy(app)


class User(db.Model):
    '''
    sqlalchemy 的数据库model
    用户信息表
    '''
    __tablename__ = "user_info"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone = db.Column(db.String(15), nullable=False, unique=True)
    name = db.Column(db.String(64), nullable=True)
    passwd = db.Column(db.String(64), nullable=False)


def create_token(api_user):
    '''
    生成token
    :param api_user:用户id
    :return: token
    '''

    # 第一个参数是加密的因子
    # 第二个参数是有效期(秒)
    s = Serializer(SECRET_KEY, expires_in=3600)
    # 接收用户id转换与编码
    token = s.dumps({"id": api_user}).decode("ascii")
    return token


def verify_token(token):
    '''
    校验token
    :param token:
    :return: 用户信息 or None
    '''

    # 参数为参数是加密的因子，与加密的一致
    s = Serializer(SECRET_KEY)
    try:
        # 转换为字典
        data = s.loads(token)
    except Exception:
        return None
    # 拿到转换后的数据，根据模型类去数据库查询用户信息
    user = User.query.get(data["id"])
    return user


# 登录校验装饰器
def login_required(view_func):
    @functools.wraps(view_func)
    def verify_token(*args, **kwargs):
        try:
            # 从用户的cookie中获取token值
            token = request.cookies.get("y-token")
        except Exception:
            # 没接收的到token,给调用方抛出错误
            return jsonify(code=4103, msg='缺少参数token')

        s = Serializer(SECRET_KEY)
        try:
            s.loads(token)
        except Exception:
            return jsonify(code=4101, msg="登录已过期")

        return view_func(*args, **kwargs)

    return verify_token


@app.route("/register", methods=["POST"])
def register():
    '''
    用户注册接口
    接收入参为json

    接口调用示例：

    json = {
            "phone": "13888888888",
            "password": "123456",
            "name": "张三"
    }

    返回信息示例：
    注册成功：
    {'code': 0, 'msg': '成功'}
    注册失败：
    {'code': 4004, 'msg': '用户已经存在'}
    :return:
    '''
    res_dir = request.get_json()
    if res_dir is None:
        # 定义错误的返回，如果没有接收到参数则提示错误
        return jsonify(code=4103, msg="未接收到参数")
    # 获取前端传过来的参数
    phone = res_dir.get("phone")
    password = res_dir.get("password")
    name = res_dir.get("name")
    # 校验参数
    if not all([phone, password]):
        return jsonify(code=4103, msg="请填写手机号或密码")

    if not re.match(r"1[23456789]\d{9}", phone):
        return jsonify(code=4103, msg="手机号有误")

    user = User.query.filter_by(phone=phone).first()
    if user:
        return jsonify(code=4004, msg="用户已经存在")
    u = User()
    u.phone = phone
    u.name = name
    u.passwd = password
    db.session.add(u)
    db.session.commit()

    # 把token返回给前端
    return jsonify(code=0, msg="成功")


@app.route("/login", methods=["POST"])
def login():
    '''
    用户登录，调用成功则进行用户cookie的赋值

    接收入参为json

    接口调用示例：

    json = {
            "phone": "13888888888",
            "password": "123456",
    }

    返回信息示例
    登录成功：
    {'code': 0, 'msg': '成功', ’data‘:'eyJhbGciOiJIUzUxMiIsImlhdCI6MTYzNTU1MjU3MCwiZXhwIjoxNjM1NTU2MTcwfQ.eyJpZCI6Mn0.vO4bVkq67MvrvhxPuSN0ln8DO7uW9pQ2EVwx-em38yVNqfHkOFZszJ6VY6UPpzL1rkUedeaiAl2odZW9AV9ZkQ'}
    登录失败：
    {'code': 4103, 'msg': '请填写手机号或密码'}
    :return:token
    '''
    res_dir = request.get_json()
    if res_dir is None:
        # 定义错误的返回，如果没有接收到参数则提示错误
        return jsonify(code=4103, msg="未接收到参数")

    # 获取前端传过来的参数
    phone = res_dir.get("phone")
    password = res_dir.get("password")
    # 校验参数
    if not all([phone, password]):
        return jsonify(code=4103, msg="请填写手机号或密码")

    if not re.match(r"1[23456789]\d{9}", phone):
        return jsonify(code=4103, msg="手机号有误")

    user = User.query.filter_by(phone=phone).first()
    if not user:
        return jsonify(code=4004, msg="获取信息失败")

    if user is None or not password == user.passwd:
        return jsonify(code=4103, msg="手机号或密码错误")

    # 获取用户id，传入生成token的方法，并接收返回的token
    token = create_token(user.id)

    # 把token返回给前端
    r = jsonify(code=0, msg="成功", data=token)
    r.set_cookie("y-token", token)
    return r


@app.route("/user/detail")
@login_required  # 必须登录的装饰器校验
def userInfo():
    '''
    用户信息
    用户信息获取
    请求method为get
    入参为调用方的cookie，从cookie中获取y-token

    调用成功示例：

    {'code': 0, 'data': {'name': '张三', 'phone': '13888888888'}, 'msg': '成功'}

    调用失败示例：

    {'code': 4101, 'msg': '登录已过期'}

    :return:data
    '''
    # 从用户的cookie中获取token值
    token = request.cookies.get("y-token")
    # 拿到token，去换取用户信息
    user = verify_token(token)

    data = {
        "phone": user.phone,
        "name": user.name
    }

    return jsonify(code=0, msg="成功", data=data)


@app.route("/execute_sql", methods=["POST"])
def execute_sql():
    '''
    执行sql接口

    接收入参为json

    接口调用示例：

    json = {
            "sql": "select name from user_info where id=1"
    }

    返回信息示例：
    查询成功：
    {'code': 0, 'msg': '成功', 'data':[{'name': '张三'}]}

    执行非查询的sql，会回滚，并且返回空data：
    {'code': 0, 'msg': '成功', 'data':[]}

    :return:
    '''
    json_data = request.get_json()
    if json_data is None:
        # 定义错误的返回，如果没有接收到参数则提示错误
        return jsonify(code=4103, msg="未接收到参数")
    # 从接口中获取sql
    sql = json_data.get("sql")
    # 执行sql语句
    cursor = db.session.execute(sql)
    try:
        # 获取sql语句执行后的结果
        datas = cursor.fetchall()
    except:
        # 无结果返回为[]
        datas = []
    finally:
        # 回滚操作
        db.session.rollback()
    # 解析查询结果数据体  ROW --> dict
    result = [dict(zip(item.keys(), item)) for item in datas]
    return jsonify(code=0, msg="成功", data=result)


if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=9000)
