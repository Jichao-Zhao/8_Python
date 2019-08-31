# encoding:utf-8
# !/usr/local/bin/python3

# 百度云：图像搜索服务
# 应用名称：垃圾分类小助手

import urllib, urllib.request, sys
import ssl
import base64
import json


#########################################################
# 调用API前必须获取Access Token
# client_id 为官网获取的AK， client_secret 为官网获取的SK
AppId = 16902645
ApiKey = 'D3WnSSyi7r8wDhY3FvvrPWmv'
SecretKey = 'fGSXUZAzc1AP4tZV0P96lpq7YyEdOScE'
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+ApiKey+'&client_secret='+SecretKey

request = urllib.request.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()
if (content):
    #print(content)
    #print(content.decode('utf-8'))                 # 通过decode将bytes字节串转换为字符串str
    contentDict = json.loads(content)               # 借助json函数将str转换为dict

    refresh_token = contentDict["refresh_token"]    # 直接读取dict字典内需要的数据   
    expires_in = contentDict["expires_in"]
    session_key = contentDict["session_key"]
    access_token = contentDict["access_token"]      
    scope = contentDict["scope"]
    session_secret = contentDict["session_secret"]
    print(access_token)

# access_token： 要获取的Access Token；
# expires_in： Access Token的有效期(秒为单位，一般为1个月)；
#########################################################





'''
相似图检索—检索
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/realtime_search/similar/search"

# 二进制方式打开图片文件
filePath = '/Users/zhaojichao/Desktop/image.jpeg'
f = open(filePath, 'rb')
img = base64.b64encode(f.read())

params = {"image": img, "pn": "200", "rn": "100"}
params = urllib.parse.urlencode(params)
params = params.encode('utf-8')

access_token = access_token
request_url = request_url + "?access_token=" + access_token
request = urllib.request.Request(url=request_url, data=params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib.request.urlopen(request)
content = response.read()
if content:
    print (content)





