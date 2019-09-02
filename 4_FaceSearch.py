# encoding:utf-8
# !/usr/local/bin/python3

# 百度云：人脸搜索服务
# 应用名称：人脸开锁


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
AppId = 16902753
ApiKey = 'rrRIfsvmI28bPFsRsSf0rrvH'
SecretKey = 'TNMr27ErnzIHt2n4TlSZPuVG7xFZkSNS'
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+ApiKey+'&client_secret='+SecretKey
request = urllib.request.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()
if (content):
    #print(content)                                 # 打印获取到的信息
    content = content.decode('utf-8')               # 通过decode将bytes字节串转换为字符串str
    contentDict = json.loads(content)               # 借助json函数将str转换为dict
    refresh_token = contentDict["refresh_token"]    # 直接读取dict字典内需要的数据
    expires_in = contentDict["expires_in"]
    session_key = contentDict["session_key"]
    access_token = contentDict["access_token"]
    scope = contentDict["scope"]
    session_secret = contentDict["session_secret"]
    #print(access_token)

'''
人脸搜索
'''
request_url = "https://aip.baidubce.com/rest/2.0/face/v3/search"
imagePath = '/Users/zhaojichao/Desktop/face.jpeg'                           # 测试100001
#imagePath = '/Users/zhaojichao/Downloads/mmexport1565091537318.jpg'        # 测试100002
f = open(imagePath, 'rb')
img = base64.b64encode(f.read())                                            # img为bytes类型
img = img.decode('utf-8')                                                   # img为str类型
params = {  "image":img, 
            "image_type":"BASE64", 
            "group_id_list":"16_219", 
            "quality_control":"LOW", 
            "liveness_control":"NORMAL"}
params = urllib.parse.urlencode(params)                                     # 对base64数据进行urlencode处理编码之后格式为str
params = params.encode('utf-8')                                             # str转为可以提交的bytes
access_token = access_token
request_url = request_url + "?access_token=" + access_token
request = urllib.request.Request(url=request_url, data=params)
request.add_header('Content-Type', 'application/json')
response = urllib.request.urlopen(request)
content = response.read()
if content:
    print (content)
