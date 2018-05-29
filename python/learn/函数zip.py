zip()函数：
并行遍历,取得一个或多个序列为参数，将给定序列中的并排的元素配成元组，返回这些元组的列表
当参数长度不同时，zip会以最短序列的长度为准

keys = [1,2,3,4,5,6,7]
values = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']

D = {}
for (k,v) in zip(keys,values):                     ### zip(xxx,yyy)是元素为元组的列表
    D[k] = v
print(D)
>>>
{1: 'Sun', 2: 'Mon', 3: 'Tue', 4: 'Wed', 5: 'Thu', 6: 'Fri', 7: 'Sat'}
