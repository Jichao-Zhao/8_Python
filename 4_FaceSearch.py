# encoding:utf-8
# !/usr/local/bin/python3

# 百度云：人脸搜索服务
# 应用名称：人脸开锁


import urllib
import urllib.request
import sys
import ssl
import base64
import json

'''
# 调用API前必须获取Access Token
# client_id 为官网获取的AK， client_secret 为官网获取的SK
'''
AppId = 16902753
ApiKey = 'rrRIfsvmI28bPFsRsSf0rrvH'
SecretKey = 'TNMr27ErnzIHt2n4TlSZPuVG7xFZkSNS'
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + \
    ApiKey+'&client_secret='+SecretKey

request = urllib.request.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()
if (content):
    #print(content)
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
# access_token： 要获取的Access Token；
# expires_in： Access Token的有效期(秒为单位，一般为1个月)；
'''


'''
人脸搜索
'''

request_url = "https://aip.baidubce.com/rest/2.0/face/v3/search"

'''
参数	    必选	  类型	    说明
image	    是	    string	  图片信息(数据大小应小于10M 分辨率应小于1920*1080)
image_type	是	    string	  图片类型    BASE64:图片的base64值;
                                        URL:图片的 URL( 下载图片时可能由于网络原因导致下载图片时间过长)
                                        FACE_TOKEN: face_token 人脸标识
'''

params = "{\"image\":\"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3579741842,3421684008&fm=26&gp=0.jpg\",\"image_type\":\"URL\",\"group_id_list\":\"16_219,group_233\",\"quality_control\":\"LOW\",\"liveness_control\":\"NORMAL\"}"
'''
经常出现错误提示：POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type str.
将params进行utf-8编码即可，将str--->bytes
'''
params = params.encode('utf-8')
access_token = access_token
request_url = request_url + "?access_token=" + access_token
request = urllib.request.Request(url=request_url, data=params)
request.add_header('Content-Type', 'application/json')
#print(type(request)
response = urllib.request.urlopen(request)
content = response.read()
if content:
    print (content)
