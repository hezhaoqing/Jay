JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式。

在python中，专门处理json格式的模块:json 和 picle模块

Json   模块提供了四个方法： dumps、dump、loads、load
pickle 模块也提供了四个  ：dumps、dump、loads、load
                                       ### 两模块用法相同
                                       ### 区别是：json模块序列化的数据更通用，picle模块序列化的数据仅python可用，但功能强大，可以序列化函数。


1.dumps() 和 dump()
dumps和dump都是序列化方法
       dumps 只完成了序列化为str，
       dump  则必须传文件描述符，将序列化的str，保存到文件中

>>> import json
>>> json.dumps([])                     ### dumps可以格式化所有的基本数据类型为【字符串】
'[]'

a = {"name":"Jay", "age":39}
with open("test.txt", "w") as f:
    f.write(json.dumps(a, indent=4))   ### indent，默认为None，小于等于0为零个空格
    json.dump(a,f,indent=4)            ### 和上面效果一样。dump必须传入f,把a序列化之后写入f.


       
2.loads() 和 load()
loads和load 则是反序列化方法
       loads 只完成了反序列化，
       load  只接收文件描述符，完成了读取文件和反序列化
       
>>> json.loads('{"name":"Jay", "age":39}')
{'age': 39, 'name': 'Jay'}             ### python3返回的结果
{u'age': 39, u'name': u'Jay'}          ### python2返回的结果。经查是编码问题，2的json库会把字符串反序列化为Unicode编码。
