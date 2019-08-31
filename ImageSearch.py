# -*- coding: UTF-8 -*-
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
ApiKey = 'rrRIfsvmI28bPFsRsSf0rrvH'
SecretKey = 'TNMr27ErnzIHt2n4TlSZPuVG7xFZkSNS'
AppId = 16902645
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+ApiKey+'&client_secret='+SecretKey
request = urllib.request.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()
if (content):
    #print(content)
    #print(content.decode('utf-8'))                 # 通过decode将bytes字节串转换为字符串str
    contentDict = json.loads(content)               # 借助json函数将str转换为dict
    access_token = contentDict["access_token"]      # 直接读取dict字典内需要的数据
    print(access_token)

# access_token： 要获取的Access Token；
# expires_in： Access Token的有效期(秒为单位，一般为1个月)；
#########################################################




'''
#########################################################相同图检索—检索
request_url = "https://aip.baidubce.com/rest/2.0/realtime_search/same_hq/search"

# 二进制方式打开图片文件
f = open('/Users/zhaojichao/Desktop/红笔.png', 'rb')


img = base64.b64encode(f.read())


params = {"image": img}
params = urllib.parse.urlencode(params)

access_token = '24.141091b91c31ba757592be819bc0da76.2592000.1566918047.282335-16902645'
request_url = request_url + "?access_token=" + access_token
request = urllib.request.Request(url=request_url, data=params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
response = urllib.request.urlopen(request)
content_result = response.read()
if (content_result):
    print(content_result)
#########################################################
'''
