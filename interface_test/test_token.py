#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '霍格沃兹测试开发学社-蚊子'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import pytest
import requests


class TestToken:

    def test_token(self):
        # 定义凭证信息
        corpid = "ww75abb8519b57cec6"
        corpsecret = "vvavK-3lew1LhtP2sLdfkieOEe8CJy5hJpdJ2ceKiEI"
        # 组装url
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"

        # 发起get请求
        res = requests.get(url=url)

        # 打印获得的结果

        print(res.text)
        print(res.json())
        assert res.json()["errcode"] == 0

    def test_token2(self):
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

        # 打印获得的结果

        print(res.text)
        print(res.json())
        assert res.json()["errcode"] == 0

    @pytest.mark.parametrize("corpid, corpsecret, expect", [("", "vvavK-3lew1LhtP2sLdfkieOEe8CJy5hJpdJ2ceKiEI", 41002),
                                                            ("xxxxxx11111",
                                                             "vvavK-3lew1LhtP2sLdfkieOEe8CJy5hJpdJ2ceKiEI", 40013)])
    def test_fail(self, corpid, corpsecret, expect):
        # 定义url
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        # 定义入参
        param = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }
        # 发起get请求
        res = requests.get(url=url, params=param)

        # 打印获得的结果

        print(res.text)
        print(res.json())
        assert res.json()["errcode"] == expect
