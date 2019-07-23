# -*- coding: UTF-8 -*-
# !/usr/local/bin/python3

import urllib
import urllib.request
import time
import base64

#UUID采用当前程序运行时间，用于防止重放攻击，开发者可根据自己需求，自定义字符串
UUID = str(time.time())
#API产品路径
host = 'http://rubbish.market.alicloudapi.com'
path = '/ai_market/ai_image_universal/rubbish/v1'
#阿里云APPCODE
appcode = 'f2334abe04d547b0a8694349a0b9a078'			#此服务的AppCode
bodys = {}
url = host + path

#内容数据类型，如：0，则表示BASE64编码；1，则表示图像文件URL链接

#启用BASE64编码方式进行识别
#内容数据类型是BASE64编码
#f = open(r'图片文件', 'rb')
#contents = base64.b64encode(f.read())
#f.close()
#bodys['IMAGE'] = contents
#bodys['IMAGE_TYPE'] = '0'

#启用URL方式进行识别
#内容数据类型是图像文件URL链接
bodys['IMAGE'] = 'https://images-na.ssl-images-amazon.com/images/I/51RCosrIe7L._SY550_.jpg'
bodys['IMAGE_TYPE'] = '1'

post_data = urllib.parse.urlencode(bodys).encode('utf-8')
request = urllib.request.Request(url, post_data)
request.add_header('Authorization', 'APPCODE ' + appcode)
request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
request.add_header('X-Ca-Nonce', UUID)
response = urllib.request.urlopen(request)
content = response.read()
if (content):
    print(content.decode('utf-8'))