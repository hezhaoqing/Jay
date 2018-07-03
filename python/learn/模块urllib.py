urllib模块中的方法:




1.
urllib.urlopen(url[,data[,proxies]]）
打开一个url，返回一个文件对象，然后可以进行类似文件对象的操作。
urlopen 返回对象提供的方法：
-         read() , readline() ,readlines() , fileno() , close() ：这些方法的使用方式与文件对象完全一样
-         info()：返回一个httplib.HTTPMessage对象，表示远程服务器返回的头信息
-         getcode()：返回Http状态码。
-         geturl()：返回请求的url




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





