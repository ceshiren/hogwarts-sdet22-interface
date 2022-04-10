#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '霍格沃兹测试开发学社-蚊子'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import pytest
import requests


class TestDepartment:

    def setup_class(self):
        # 定义凭证信息
        corpid = "ww75abb8519b57cec6"
        corpsecret = "vvavK-3lew1LhtP2sLdfkieOEe8CJy5hJpdJ2ceKiEI"
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        param = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }
        # 发起get请求
        res = requests.get(url=url, params=param)

        self.token = res.json()["access_token"]

    def test_create_department(self):
        # 定义url：
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"

        # 定义param
        param = {
            "access_token": self.token
        }

        # 定义请求包体

        create_body = {
            "name": "广州研发中心1",
            "name_en": "RDGZ1",
            "parentid": 1,
            "order": 1,
            "id": 45
        }

        # 发起请求

        res = requests.post(url=url, params=param, json=create_body)

        # 断言响应
        assert res.json()["errcode"] == 0

    @pytest.mark.parametrize("name,name_en,parentid,order,_id,expect",
                             [("技术部1t6yuaambg54321", "JISHUxxx", 1, 1, 566, 0)])
    def test_create_department_with_param(self, name, name_en, parentid, order, _id, expect):
        # 定义url：
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"

        # 定义param
        param = {
            "access_token": self.token
        }

        # 定义请求包体

        create_body = {
            "name": name,
            "name_en": name_en,
            "parentid": parentid,
            "order": order,
            "id": _id
        }

        # 发起请求

        res = requests.post(url=url, params=param, json=create_body)

        # 断言响应
        assert res.json()["errcode"] == expect

    def test_del_department(self):
        # 定义url
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"

        # 定义param
        param = {
            "access_token": self.token,
            "id": 45
        }

        # 发起删除动作

        res = requests.get(url=url, params=param)

        # 断言删除动作是否成功

        assert res.json()["errcode"] == 0
