#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '霍格沃兹测试开发学社-蚊子'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

from genson import SchemaBuilder

build = SchemaBuilder()
build.add_object({"a": 1, "b": "aaaa", "c": "", "d": None})
build.add_object({"a": "1", "b": "bbb", "c": 1})
print(build.to_json(indent=2))


