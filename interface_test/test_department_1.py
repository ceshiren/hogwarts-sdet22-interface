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

    def setup(self):
        # 定义department_id
        self.department_id = 588
        try:
            # 尝试进行定义的id的删除，排除干扰
            self.del_department(self.department_id)
        except Exception as e:
            print(e)

    # def teardown(self):
    #     try:
    #         self.del_department(self.department_id)
    #     except Exception as e:
    #         print(e)

    def del_department(self, _id):
        # 定义url
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"

        # 定义param
        param = {
            "access_token": self.token,
            "id": _id
        }

        # 发起删除动作

        res = requests.get(url=url, params=param)

        print(res.json())

    def create_depart(self, _id):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"

        # 定义param
        param = {
            "access_token": self.token
        }

        # 定义请求包体

        create_body = {
            "name": f"广州研发中心_创建{_id}",
            "name_en": f"RDGZ_create_{_id}",
            "parentid": 1,
            "order": 1,
            "id": _id
        }

        # 发起请求

        res = requests.post(url=url, params=param, json=create_body)
        print(res)

    def test_create_department(self):
        # 定义url：
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"

        # 定义param
        param = {
            "access_token": self.token
        }

        # 定义请求包体

        create_body = {
            "name": "广州研发中心_3",
            "name_en": "RDGZ_3",
            "parentid": 1,
            "order": 1,
            "id": self.department_id
        }

        # 发起请求

        res = requests.post(url=url, params=param, json=create_body)

        # 断言响应
        assert res.json()["errcode"] == 0

    def test_update_department(self):
        self.create_depart(self.department_id)
        # 定义url：
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/update"

        # 定义param
        param = {
            "access_token": self.token
        }

        # 定义请求包体

        create_body = {
            "name": f"广州研发中心_update{self.department_id}",
            "name_en": f"RDGZ1_update_{self.department_id}",
            "parentid": 1,
            "order": 1,
            "id": self.department_id
        }

        # 发起请求

        res = requests.post(url=url, params=param, json=create_body)

        # 断言响应
        assert res.json()["errcode"] == 0
