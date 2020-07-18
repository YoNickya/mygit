# coding:utf-8
# 这个是post请求出来直接就有的数据
import requests
import json
from urllib import  parse

url = "http://172.19.69.128:8888/bfs/dayCheckService/dayCheckAccount"
data1 =[
    {
        "DOC_NUMBER": "2018/08/31付款凭证1289",
        "kjkm": "10020101",
        "company": "18",
        "amount": 23489627.9,
        "dorc": "贷",
        "use": "",
        "bytter_account": "1001180022085145510",
        "create_time": "",
        "g_date": "2018/08/31",
        "data_source": "NC"
    
    }
]

data1 = json.dumps(data1)

print("调试")
r = requests.post(url,data1)

print(r)



