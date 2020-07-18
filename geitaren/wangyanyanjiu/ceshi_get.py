# coding:utf-8
# 这个是get请求不带参数,也需要url转码显示
import requests
import json
from urllib import  parse

url = "http://172.22.2.10:8763/getJyAocT2001/AQ1170/2019-10-1/2019-10-2/AQ/N/6/N/N"

r = requests.get(url)

print(r)

print(parse.unquote_plus(r.text))



