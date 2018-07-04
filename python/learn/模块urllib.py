********************
*      urllib      *
********************
urllib模块中的方法:

1.
urllib.urlopen(url[,data[,proxies]]）
打开一个url，返回一个文件对象，然后可以进行类似文件对象的操作。
urlopen 返回对象提供的方法：
-         read() , readline() ,readlines() , fileno() , close() ：这些方法的使用方式与文件对象完全一样
-         info()：返回一个httplib.HTTPMessage对象，表示远程服务器返回的头信息
-         getcode()：返回Http状态码。
-         geturl()：返回请求的url
简单示例：
import urllib               
google = urllib.urlopen('http://www.google.com')
print 'http header:/n', google.info()
print 'http status:', google.getcode()
print 'url:', google.geturl()
for line in google:
    print line,
google.close()

2.
urllib.urlretrieve(url[,filename[,reporthook[,data]]])
urlretrieve方法将url定位到的html文件下载到你本地的硬盘中。如果不指定filename，则会存为临时文件。
urlretrieve()返回一个二元组(filename,mine_hdrs)

不指定filename，临时存放到/tmp下
>>> file = urllib.urlretrieve('http://www.google.com.hk/')
>>> type(file)
<type 'tuple'>
>>> file[0]
'/tmp/tmp8eVLjq'
>>> file[1]
<httplib.HTTPMessage instance at 0xb6a363ec>

指定filename，存放到指定位置
>>> file = urllib.urlretrieve('http://www.google.com.hk/',filename='/home/python/urllib/google.html')
>>> type(file)
<type 'tuple'>
>>> file[0]
'/home/python/urllib/google.html'
>>> file[1]
<httplib.HTTPMessage instance at 0xb6e2c38c>


3.
urllib.urlcleanup()
清除由于urllib.urlretrieve()所产生的缓存


4.
urllib.quote(url)和urllib.quote_plus(url)
将url数据获取之后，将其编码，从而适用于URL字符串中，使其能被打印和被web服务器接受。

>>> urllib.quote('http://www.baidu.com')
'http%3A//www.baidu.com'
>>> urllib.quote_plus('http://www.baidu.com')
'http%3A%2F%2Fwww.baidu.com'


5.
urllib.unquote(url)和urllib.unquote_plus(url)
与4相反。

               
6.
urllib.urlencode(query)
将 键值对 以连接符 & 划分  
可以与urlopen结合以实现post方法和get方法

GET:
>>> import urllib
>>> params=urllib.urlencode({'spam':1,'eggs':2,'bacon':0})
>>> params
'eggs=2&bacon=0&spam=1'                                              ### 将key:value,key:value 转化为 key=value&key=value格式
>>> f=urllib.urlopen("http://python.org/query?%s" % params)
>>> print f.read()

POST:
>>> import urllib
>>> parmas = urllib.urlencode({'spam':1,'eggs':2,'bacon':0})
>>> f=urllib.urlopen("http://python.org/query",parmas)
>>> f.read()


               
               
               


********************
*      urllib2     *
********************
-          urllib 和urllib2都是接受URL请求的相关模块，
-          但是urllib2可以接受一个Request类的实例来设置URL请求的headers，
-          urllib仅可以接受URL，所以不可以伪装你的User Agent字符串等。
-          urllib提供urlencode方法用来GET查询字符串的产生，而urllib2没有。
-          这是为何urllib常和urllib2一起使用的原因。
-          目前的大部分http请求都是通过urllib2来访问的。

示例：
import urllib
import urllib2
url = 'http://www.someserver.com/cgi-bin/register.cgi'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'             # 将user_agent写入头信息
values = {'name' : 'zhoujielun','password':'123456'}                      # post方式
headers = { 'User-Agent' : user_agent }
data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
get_page = response.read()
               
               
               
               

               
               
********************
*      Python3     *
********************
urllib库和urilib2库合并成了urllib库。
其中
urllib2.urlopen()变成了urllib.request.urlopen()
urllib2.Request()变成了urllib.request.Request()
