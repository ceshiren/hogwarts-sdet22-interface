#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '霍格沃兹测试开发学社-蚊子'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import pymysql
import requests


def query_db(sql):
    conn = pymysql.Connect(host="47.92.149.0",port=3366,database="test_db",
                           user="root",password="123456",charset="utf8")
    cursor = conn.cursor()
    cursor.execute(sql)
    datas = cursor.fetchall()
    cursor.close()
    conn.close()
    return datas

def test_query():
    sql = "select * from user_info where phone='13544478882'"
    print(query_db(sql))

def test_register():
    data = {
        "phone": "12345678912",
        "password": "123456",
        "name": "cat"
    }
    r = requests.post(url="http://47.92.149.0:9000/register",json=data)
    assert r.json()["code"] == 0
    sql = "select * from user_info where phone='12345678912'"
    assert len(query_db(sql)) == 1