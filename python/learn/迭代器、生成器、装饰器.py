1 迭代器

什么是可迭代对象（Iterable）？
可以直接作用于for循环的对象统称为可迭代对象，即Iterable。
　　# 一是集合数据类型，如list、tuple、dict、set、str等；
　　# 二是generator，包括生成器和带yield的generator function。

什么又是迭代器（Iterator）？
可以被next()函数调用并不断返回下一个值（直到没有数据时抛出StopIteration错误）的对象称为迭代器，即Iterator。

Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
# 可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，
# 所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
# Iterable 可以通过iter()函数转换得到 Iterator





2 生成器

generator 就是 iterator 的一种,以更优雅的方式实现的 iterator 。





3 装饰器




