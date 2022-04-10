#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '霍格沃兹测试开发学社-蚊子'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

import logging
import os

# 实例化logger对象
from interface_test.api_object.utils.utils import Utils

logger = logging.getLogger(__name__)
# 定义日志文件路径
log_path = Utils.get_log_path()
# 判断路径是否存在，不存在就创建

if not os.path.exists(log_path):
    os.mkdir(log_path)

# 绑定log的handler
file_handler = logging.FileHandler(filename=f"{log_path}/api_object.log", encoding="utf-8")

# 输出的formatter

formatter = logging.Formatter('[%(asctime).19s] %(process)d:%(levelname).1s %(filename)s:%(lineno)d:%(funcName)s: %(message)s]')

# 日志格式与句柄的绑定

file_handler.setFormatter(formatter)

# 控制台句柄定义

steam_handler = logging.StreamHandler()
# 日志格式与句柄的绑定
steam_handler.setFormatter(formatter)

# 与logger进行绑定

logger.addHandler(file_handler)
logger.addHandler(steam_handler)

# 设置展示/写入文件的日志的级别

logger.setLevel(logging.INFO)