#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '霍格沃兹测试开发学社-蚊子'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

from interface_test.api_object.apis.wework_api import Wework
from interface_test.api_object.utils.utils import Utils


class Department(Wework):

    def __init__(self):
        super().__init__()
        yaml_data = Utils.get_yaml_data("corp_data.yaml")
        self.get_token(yaml_data.get("corpid").get("yinian"), yaml_data.get("secret").get("department"))

    def create(self, _id):
        '''
        定义部门的创建
        :return:
        '''
        # url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        # # 定义param
        # param = {
        #     "access_token": self.token
        # }
        #
        # # 定义请求包体
        #
        # create_body = {
        #     "name": f"广州研发中心_创建{_id}",
        #     "name_en": f"RDGZ_create_{_id}",
        #     "parentid": 1,
        #     "order": 1,
        #     "id": _id
        # }

        # 发起请求

        req = {
            "method": "POST",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/create",
            "params": {
                "access_token": self.token
            },
            "json": {
                "name": f"广州研发中心_创建{_id}",
                "name_en": f"RDGZ_create_{_id}",
                "parentid": 1,
                "order": 1,
                "id": _id
            }
        }
        res = self.send_api(req)
        # res = requests.post(url=url, params=param, json=create_body)
        return res.json()

    def update(self, _id):
        '''
        定义部门的更新
        :return:
        '''
        # url = "https://qyapi.weixin.qq.com/cgi-bin/department/update"
        # # 定义param
        # param = {
        #     "access_token": self.token
        # }
        #
        # # 定义请求包体
        #
        # update_body = {
        #     "name": f"广州研发中心_update{_id}",
        #     "name_en": f"RDGZ1_update_{_id}",
        #     "parentid": 1,
        #     "order": 1,
        #     "id": _id
        # }
        #
        # # 发起请求
        #
        # res = requests.post(url=url, params=param, json=update_body)
        # return res.json()

        req = {
            "method": "POST",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/update",
            "params": {
                "access_token": self.token
            },
            "json": {
                "name": f"广州研发中心_update{_id}",
                "name_en": f"RDGZ1_update_{_id}",
                "parentid": 1,
                "order": 1,
                "id": _id
            }
        }
        res = self.send_api(req)
        return res.json()

    def get(self):
        '''
        获取部门的列表
        :return:
        '''
        # url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
        # param = {
        #     "access_token": self.token
        # }
        # res = requests.get(url=url, params=param)

        req = {
            "method": "GET",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/list",
            "params": {
                "access_token": self.token
            }
        }
        res = self.send_api(req)
        return res.json()

    def delete(self, _id):
        '''
        删除部门
        :return:
        '''
        # url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
        #
        # # 定义param
        # param = {
        #     "access_token": self.token,
        #     "id": _id
        # }
        #
        # # 发起删除动作
        #
        # res = requests.get(url=url, params=param)
        #
        # return res.json()

        req = {
            "method": "GET",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/delete",
            "params": {
                "access_token": self.token,
                "id": _id
            }
        }
        res = self.send_api(req)
        return res.json()
