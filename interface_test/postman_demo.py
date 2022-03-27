#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '霍格沃兹测试开发学社-蚊子'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import requests
import json

url = "https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token=PNY3v5F_oqhFo6voiLQnsNo9W5lIM8miNIhgNeGRAmbUoXsdwy6xFipKrfUicFRAkCm2tnBonx5pp2WTrw3VK5lZlgxO1xkDkJvVWZ683RoYeQdVX1Maxqczx3i87wN-oKeH8V9QM3B8Uo6XxWotS39froAaT7SAtHs7Da1KSZxovk7wzpqiCdPmzUPENR07actai5Wqr06xGMBBnXLlqQ"

payload = "{\n   \"name\": \"dapartpost1\",\n   \"name_en\": \"postman1\",\n   \"parentid\": 1,\n   \"order\": 1,\n   \"id\": 88\n}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)