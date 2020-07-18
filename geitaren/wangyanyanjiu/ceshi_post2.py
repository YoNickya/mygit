# coding:utf-8
# 这个是post请求出来有“%7B%22resu%38A%9F%22%7D%5D%7D”的数据，需要解码
import requests
import json
from urllib import  parse

url = "http://172.22.2.10:8888/dw/ncInfoService/ItfAccsubjInfo"
data = {"datas":[{
 "fbs_code":"400002",
 "fbs_name":"人力成梵蒂冈个符合规范本",
 "valid_sign":"1"
}]
}

header = {"Content-Type":"application/json"}
data = json.dumps(data)
data1=[]
data1.append(data)

data2=data1[0]
r = requests.post(url, data=data2, headers=header).content.decode()
print(r)

# 数据需要url解码，才能显示我们能看懂的数据
r1 = parse.unquote_plus(r)
print(r1)

