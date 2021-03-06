# encoding:utf-8
# !/usr/local/bin/python3

# 百度云：文字识别服务
# 应用名称：文字识别练习项目

import urllib3
from urllib.parse import urlencode
import urllib
import urllib.request
import sys
import ssl
import base64
import json

'''
# 调用API前必须获取Access Token
# client_id 为官网获取的AK， client_secret 为官网获取的SK
# access_token： 要获取的Access Token；
# expires_in： Access Token的有效期(秒为单位，一般为1个月)；
'''
APPId = 17165172
ApiKey = 'uck9A45flml7ITBQ8VaLUojf'
SecretKey = 'p19Nl1Rz1DGGMKepK3lNDWk8TogqankG'
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+ApiKey+'&client_secret='+SecretKey
request = urllib.request.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()
if (content):
    #print(content)                                 # 打印获取到的信息
    # 通过decode将bytes字节串转换为字符串str
    content = content.decode('utf-8')
    contentDict = json.loads(content)               # 借助json函数将str转换为dict
    refresh_token = contentDict["refresh_token"]    # 直接读取dict字典内需要的数据
    expires_in = contentDict["expires_in"]
    session_key = contentDict["session_key"]
    access_token = contentDict["access_token"]
    scope = contentDict["scope"]
    session_secret = contentDict["session_secret"]
    #print(access_token)

'''
手写文字识别
# 所有图片均需要base64编码、去掉编码头后再进行urlencode。
'''
request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/handwriting"        #手写文字识别接口
imagePath = '/Users/zhaojichao/Desktop/ocrtest.jpg'                           # 测试100001
f = open(imagePath, 'rb')
# img为bytes类型
img = base64.b64encode(f.read())
# img为str类型
img = img.decode('utf-8')
params = {"image": img}
          #"recognize_granularity": "BASE64",
          #"words_type": "16_219"}
# 对base64数据进行urlencode处理编码之后格式为str
params = urllib.parse.urlencode(params)
# str转为可以提交的bytes
params = params.encode('utf-8')
access_token = access_token
request_url = request_url + "?access_token=" + access_token
request = urllib.request.Request(url=request_url, data=params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib.request.urlopen(request)
content = response.read()
if content:
    # 返回数据为bytes，需要转换为str
    content = content.decode('utf-8')
    print(content)
