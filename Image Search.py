# -*- coding: UTF-8 -*-
# !/usr/local/bin/python3

import urllib, urllib.request, sys
import ssl
import base64

#########################################################
# 获取Access Token
# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=D3WnSSyi7r8wDhY3FvvrPWmv&client_secret=fGSXUZAzc1AP4tZV0P96lpq7YyEdOScE'
request = urllib.request.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()
if (content):
    #print(content)
# access_token： 要获取的Access Token；
# expires_in： Access Token的有效期(秒为单位，一般为1个月)；
#########################################################



#########################################################相同图检索—检索
	request_url = "https://aip.baidubce.com/rest/2.0/realtime_search/same_hq/search"

# 二进制方式打开图片文件
f = open('/Users/zhaojichao/Desktop/红笔.png', 'rb')


img = base64.b64encode(f.read())


params = {"image":img}
params = urllib.parse.urlencode(params)

access_token = '24.141091b91c31ba757592be819bc0da76.2592000.1566918047.282335-16902645'
request_url = request_url + "?access_token=" + access_token
request = urllib.request.Request(url=request_url, data=params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
response = urllib.request.urlopen(request)
content_result = response.read()
if (content_result):
    print (content_result)
#########################################################




