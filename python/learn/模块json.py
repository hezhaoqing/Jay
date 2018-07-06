JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式。

在python中，专门处理json格式的模块:json 和 picle模块

Json   模块提供了四个方法： dumps、dump、loads、load
pickle 模块也提供了四个  ：dumps、dump、loads、load


1.dumps() 和 dump()
dumps和dump都是序列化方法
       dumps 只完成了序列化为str，
       dump  则必须传文件描述符，将序列化的str，保存到文件中

>>> import json
>>> json.dumps([])                     ### dumps可以格式化所有的基本数据类型为【字符串】
'[]'

a = {"name":"Tom", "age":23}
with open("test.txt", "w") as f:
    f.write(json.dumps(a, indent=4))   ### indent，默认为None，小于等于0为零个空格
    json.dump(a,f,indent=4)            ### 和上面效果一样。dump必须传入f,把a序列化之后写入f.
