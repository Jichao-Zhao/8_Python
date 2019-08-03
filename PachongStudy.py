"""
#	urllib：urllib库，它是Python内置的HTTP请求库，也就是说不需要额外安装即可使用。它包含如下4个模块。
#	request：它是最基本的HTTP请求模块，可以用来模拟发送请求。就像在浏览器里输入网址然后回车一样，只需要给库方法传入URL以及额外的参数，就可以模拟实现这个过程了。
#	error：异常处理模块，如果出现请求错误，我们可以捕获这些异常，然后进行重试或其他操作以保证程序不会意外终止。
#	parse：一个工具模块，提供了许多URL处理方法，比如拆分、解析、合并等。
#	robotparser：主要是用来识别网站的robots.txt文件，然后判断哪些网站可以爬，哪些网站不可以爬，它其实用得比较少。
"""
import urllib.request
import urllib.parse

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
response = urllib.request.urlopen("https://httpbin.org/post", data = data)


print(response.read())














