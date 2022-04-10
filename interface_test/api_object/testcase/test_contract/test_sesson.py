#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '霍格沃兹测试开发学社-蚊子'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import requests


def test_login():
    data = {
        "phone": "13544478882",
        "password": "1234561"
    }
    r = requests.post(url="http://47.92.149.0:9000/login", json=data)
    print(r.json())


def test_search_fail():
    r = requests.get(url="http://47.92.149.0:9000/user/detail")
    print(r.json())


def test_search_success():
    session = requests.session()
    data = {
        "phone": "13544478882",
        "password": "123456"
    }
    r = session.post(url="http://47.92.149.0:9000/login", json=data)
    print(r.json())
    print(r.cookies)
    print(r.headers)
    r = session.get(url="http://47.92.149.0:9000/user/detail")
    print(r.json())
