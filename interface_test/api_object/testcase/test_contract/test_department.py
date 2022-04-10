#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '霍格沃兹测试开发学社-蚊子'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import pytest

from interface_test.api_object.apis.contract.department import Department
from interface_test.api_object.utils.log_util import logger
from interface_test.api_object.utils.utils import Utils


class TestDepartment:

    def setup(self):
        self.department_id = 588
        self.dapart = Department()
        try:
            # 尝试进行定义的id的删除，排除干扰
            self.dapart.delete(self.department_id)
        except Exception as e:
            logger.warning("没有待删除的部门")

    # @pytest.mark.parametrize()
    def test_create_department(self):
        assert self.dapart.create(self.department_id)["errcode"] == 0
        obj = self.dapart.get()
        department_list = Utils.jsonpath_util(obj, "$..department..id")
        assert self.department_id in department_list
