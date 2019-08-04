"""
#	urllib：urllib库，它是Python内置的HTTP请求库，也就是说不需要额外安装即可使用。它包含如下4个模块。
#	request：它是最基本的HTTP请求模块，可以用来模拟发送请求。就像在浏览器里输入网址然后回车一样，只需要给库方法传入URL以及额外的参数，就可以模拟实现这个过程了。
#	error：异常处理模块，如果出现请求错误，我们可以捕获这些异常，然后进行重试或其他操作以保证程序不会意外终止。
#	parse：一个工具模块，提供了许多URL处理方法，比如拆分、解析、合并等。
#	robotparser：主要是用来识别网站的robots.txt文件，然后判断哪些网站可以爬，哪些网站不可以爬，它其实用得比较少。
"""
import urllib.request
import urllib.parse
import socket
import urllib.error

"""
#	语法：urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
#	功能：获取网站的信息
#	url：网站的URL地址
#	data：附加数据，data参数是可选的。如果要添加该参数，并且如果它是字节流编码格式的内容，即bytes类型，则需要通过bytes()方法转化。另外，如果传递了这个参数，则它的请求方式就不再是GET方式，而是POST方式。
#	timeout：超时时间
"""
response = urllib.request.urlopen("https://www.python.org")

#	输出返回的网页内容
print(response.read().decode('utf-8'))
#	输出响应的类型：<class 'http.client.HTTPResponse'>
print(type(response))
#	输出响应的状态码，如200代表请求成功，404代表网页未找到等。
print(response.status)
#	输出响应的头信息
print(response.getheaders())
#	输出通过调用getheader()方法并传递一个参数Server获取了响应头中的Server值，结果是nginx，意思是服务器是用Nginx搭建的。
print(response.getheader("Server"))

#	这里我们传递了一个参数word，值是hello。它需要被转码成bytes（字节流）类型。其中转字节流采用了bytes()方法，该方法的第一个参数需要是str（字符串）类型，需要用urllib.parse模块里的urlencode()方法来将参数字典转化为字符串；第二个参数指定编码格式，这里指定为utf8。
data = bytes(urllib.parse.urlencode({"word": "hello"}), encoding = "utf-8")
response_data = urllib.request.urlopen("https://httpbin.org/get", timeout=1)

print(response.read())

try:
	response_timeout = urllib.request.urlopen("https://httpbin.org/get", timeout = 0.1)
except urllib.error.URLError as e:
	if isinstance(e.reason, socket.timeout):
		print("Time Out")


request = urllib.request.Request("https://python.org")
response_request = urllib.request.urlopen(request)
print(response_request.read().decode("utf-8"))

'''
#	利用urlopen()可以实现最基本请求的发起，但这几个简单的参数不足以构建一个完整的请求。
#	如果请求中加入Headers等信息，就可以利用更加强大的Request类来构建
#	class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
#	url：用于请求URL，这是必传参数，其他都是可选参数
#	data：如果data要传，必须传bytes(字节流)类型的。如果它是字典，可以先用urllib.parse模块里的urlencode()编码
#	headers：是一个字典，它是请求头，我们可以在构造请求时通过headers参数直接构造，也可通过调用请求实例的add_header()方法添加
#	添加请求头最常用的方法就是通过修改User-Agent来伪装浏览器，默认的User-Agent时Python-urllib，我们可以通过修改它来伪装浏览器
#	比如伪装火狐浏览器，可把它设置为：Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11
#	origin_req_host：指的是请求方的host名称或者IP地址
#	unverifiable：表示这个请求是否是无法验证的，默认False，意思就是说用户没有足够权限来选择接收这个请求的结果
#	method：是一个字符串，用来指示请求使用的方法，比如GET、POST、和PUT等
'''
url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))









