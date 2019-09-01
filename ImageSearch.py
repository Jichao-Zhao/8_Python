# encoding:utf-8
# !/usr/local/bin/python3

# 百度云：图像搜索服务
# 应用名称：垃圾分类小助手

import urllib, urllib.request, sys
import ssl
import base64
import json

'''
# 调用API前必须获取Access Token
# client_id 为官网获取的AK， client_secret 为官网获取的SK
'''
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
    content = content.decode('utf-8')               # 通过decode将bytes字节串转换为字符串str
    contentDict = json.loads(content)               # 借助json函数将str转换为dict

    refresh_token = contentDict["refresh_token"]    # 直接读取dict字典内需要的数据   
    expires_in = contentDict["expires_in"]
    session_key = contentDict["session_key"]
    access_token = contentDict["access_token"]      
    scope = contentDict["scope"]
    session_secret = contentDict["session_secret"]
    print(content)
'''
# access_token： 要获取的Access Token；
# expires_in： Access Token的有效期(秒为单位，一般为1个月)；

# 返回数据示例
b'{"refresh_token":"25.2f1bf356118efa17944e487bc94c686a.315360000.1882688238.282335-16902645",
"expires_in":2592000,
"session_key":"9mzdWrhNnIY0KvjOQJKMoALs\\/ym\\/c1cfKIqM6EH7Sd6Pz7oWaN4C6Wlig4t8U1rMYS3tKRWweBGs2UlHyIQ+TuLlWpgZjw==",
"access_token":"24.ad3200bcf4cce0e05bd9fc4fa77fa5f6.2592000.1569920238.282335-16902645",
"scope":"vis-faceverify_FACE_Police public brain_all_scope vis-classify_\\u5b9e\\u65f6\\u68c0\\u7d22-\\u76f8\\u4f3c brain_realtime_same_hq brain_realtime_similar brain_realtime_product wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test\\u6743\\u9650 vis-classify_flower lpq_\\u5f00\\u653e cop_helloScope ApsMis_fangdi_permission smartapp_snsapi_base iop_autocar oauth_tp_app smartapp_smart_game_openapi oauth_sessionkey smartapp_swanid_verify smartapp_opensource_openapi smartapp_opensource_recapi fake_face_detect_\\u5f00\\u653eScope",
"session_secret":"af38edc68985208232c6f7d69367f300"}\n'

# 经过json.load()解码后的数据
{"refresh_token":"25.fbd83dbd4365869dede04021923e4dfb.315360000.1882688536.282335-16902645",
"expires_in":2592000,
"session_key":"9mzdDx3Gdvd5IKP7UrrEJ1g0OtjAXTLbUchCSztv2CEI3Li\/eD3ifBuKtKjR6ChctvQnlJojPTuNqTyIkrNaXlaETiX6TQ==",
"access_token":"24.499e10f691340c829d0cbd1af897a45d.2592000.1569920536.282335-16902645",
"scope":"vis-faceverify_FACE_Police public brain_all_scope vis-classify_\u5b9e\u65f6\u68c0\u7d22-\u76f8\u4f3c brain_realtime_same_hq brain_realtime_similar brain_realtime_product wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test\u6743\u9650 vis-classify_flower lpq_\u5f00\u653e cop_helloScope ApsMis_fangdi_permission smartapp_snsapi_base iop_autocar oauth_tp_app smartapp_smart_game_openapi oauth_sessionkey smartapp_swanid_verify smartapp_opensource_openapi smartapp_opensource_recapi fake_face_detect_\u5f00\u653eScope",
"session_secret":"c41c01d5b75f3d61e9b9a639121e302e"}
'''






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





