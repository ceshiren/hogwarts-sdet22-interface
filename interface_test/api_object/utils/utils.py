#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '霍格沃兹测试开发学社-蚊子'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import os

import jsonpath
import yaml


class Utils:

    @classmethod
    def get_yaml_data(cls, yaml_file):
        '''
        封装提取yaml文件的方法
        :return: 传入文件的路径
        '''
        with open(f"{Utils.get_data_path()}/{yaml_file}", encoding="utf-8") as f:
            datas = yaml.safe_load(f)
        return datas

    @classmethod
    def get_data_path(cls):
        path = os.sep.join([os.path.dirname(os.path.abspath(__file__)), "../data"])
        return path

    @classmethod
    def get_log_path(cls):
        path = os.sep.join([os.path.dirname(os.path.abspath(__file__)), "../logs"])
        return path

    @classmethod
    def jsonpath_util(cls, obj, expr):
        return jsonpath.jsonpath(obj, expr)


if __name__ == '__main__':
    # path = Utils.get_data_path()
    print(Utils.get_yaml_data("corp_data.yaml"))
    print(Utils.get_log_path())
