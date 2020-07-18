# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 16:27
# @Author  : babi
#
# import allure
# import pytest
#
# from Params.params import Ceshiget
# from Conf.Config import Config
# from Common import Request
# from Common import Consts
# from Common import Assert
# import json
# from urllib import parse
# import requests
#
#
# class TestCeshiget:
#
#     @allure.feature('Ceshiget')
#     @allure.severity('blocker')
#     @allure.story('Ceshiget')
#     def test_ceshiget_01(self, action):
#         """
#             用例描述01：get随意一个测试
#         """
#         conf = Config()
#         data = Ceshiget()
#         test = Assert.Assertions()
#         request = Request.Request(action)
#
#         host = conf.host_get
#         req_url = 'http://' + host
#         urls = data.url
#         params = data.data
#         headers = data.header
#
#         api_url = req_url + urls[0]
#         response = request.get_request(api_url, params, headers[0])
#         r = parse.unquote_plus(response["text"])
#
#
#         assert test.assert_code(response['code'], 200)
#         # 这个需要url解码才能看出来，并且需要导入包from urllib import  parse，S代表更新成功的意思
#         assert test.assert_in_text(parse.unquote_plus(response["text"]), "查询成功,返回数据集合")
#
#         Consts.RESULT_LIST.append('True')
#
#
