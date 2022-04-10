#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '霍格沃兹测试开发学社-蚊子'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import requests

from interface_test.api_object.utils.log_util import logger


class BaseApi:

    def send_api(self, req, tools="requests"):
        '''
        对发送接口测试的工具进行封装
        :return:
        '''
        # 如果没有送工具，则默认使用requests
        # if not tools:
        #     tools = "requests"
        logger.info(f"获取到的工具为{tools}")
        logger.info(f"获取到的接口发送的数据为{req}")
        if tools == "requests":
            return requests.request(**req)
