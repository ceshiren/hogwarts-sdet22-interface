#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '霍格沃兹测试开发学社-蚊子'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import json

from genson import SchemaBuilder
from jsonschema import validate, ValidationError, SchemaError


def test_gen_genson():
    build = SchemaBuilder()
    build.add_object({"a": 1, "b": "aaaa", "c": "", "d": None})
    build.add_object({"a": "1", "b": "bbb", "c": 1})
    json.dump(build.to_schema(), open("demo_schema.json", "w", encoding="utf-8"))


def schema_validate(obj, schema):
    try:
        validate(instance=obj, schema=schema)
    except ValidationError as err:
        print(err)
        return False
    except SchemaError as err:
        print(err)
        return False
    else:
        print("schema 校验成功")
        return True


def test_genson():
    _schema = json.load(open("demo_schema.json", encoding='utf-8'))
    assert schema_validate({"a": 1, "b": 1, "c": "", "d": None}, _schema)
