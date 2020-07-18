# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 16:27
# @Author  : babi
# @File    : Test_Basic.py

import allure
import pytest

from Params.params import Storeget
from Conf.Config import Config
from Common import Request
from Common import Consts
from Common import Assert
import json
from urllib import parse
import requests


class TestStoreget:

    @allure.feature('Storeget')
    @allure.severity('blocker')
    @allure.story('Storeget')
    def test_storeget_01(self, action):
        """
            用例描述01：get查询门店(鲜食1号)
        """
        conf = Config()
        data = Storeget()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_get
        req_url = 'http://' + host
        print(req_url)
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[0]
        print(api_url)
        response = request.get_request(api_url, params[0], headers[0])
        r = parse.unquote_plus(response["text"])
        print(response)
        print(r)

        assert test.assert_code(response['code'], 200)
        # 这个需要url解码才能看出来，并且需要导入包from urllib import  parse，S代表更新成功的意思
        assert test.assert_in_text(parse.unquote_plus(response["text"]), "鲜食1号")

        Consts.RESULT_LIST.append('True')


    @allure.feature('Storeget')
    @allure.severity('blocker')
    @allure.story('Storeget')
    def test_storeget_02(self, action):
        """
            用例描述01：get查询门店无效的字符（####）
        """
        conf = Config()
        data = Storeget()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_get
        req_url = 'http://' + host
        print(req_url)
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[1]
        print(api_url)
        response = request.get_request(api_url, params[1], headers[1])
        # r = parse.unquote_plus(response["text"])
        print(response)
        # print(r)
        assert test.assert_code(response['code'], 200)
        # 这个需要url解码才能看出来，并且需要导入包from urllib import  parse，S代表更新成功的意思

        Consts.RESULT_LIST.append('True')