#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '霍格沃兹测试开发学社-蚊子'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

from interface_test.api_object.apis.base_api import BaseApi


class Wework(BaseApi):

    def __init__(self):
        self.token = None

    def get_token(self, corpid, corpsecret):
        # return: access_token的值

        # corpid = "ww75abb8519b57cec6"
        # corpsecret = "vvavK-3lew1LhtP2sLdfkieOEe8CJy5hJpdJ2ceKiEI"
        # url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        # param = {
        #     "corpid": corpid,
        #     "corpsecret": corpsecret
        # }
        # 发起get请求
        # res = requests.get(url=url, params=param)
        req = {
            "method": "GET",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": corpid,
                "corpsecret": corpsecret
            }
        }
        res = self.send_api(req)
        self.token = res.json()["access_token"]
