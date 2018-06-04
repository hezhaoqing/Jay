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

什么是装饰器（Decorator）？
本质上：是一个返回函数的高阶函数。

生产上，什么时候用装饰器？
当我们想要给一个函数func()增加某些功能，但又不希望修改func()函数的源代码的时候就需要用装饰器了。（在代码运行期间动态增加功能）


装饰器例子：
[root@svn py]# cat zsq.py 
#!/bin/env python
#coding:utf-8
import functools                                  ### 函数工具模块

def login(func):
    """
    在这里新定义一个高阶函数，
    这就是decorator
    """
    @functools.wraps(func)                        ### Python内置的functools.wraps()使 带有装饰器的函数的name属性保持不变
    def wrapper(*args, **kwargs):
        user = "hzq"                              ### 假设这是数据库中的用户名和密码
        passwd = "123"
        username = raw_input("输入用户名：")
        password = raw_input("输入密码：")
        if username == user and password == passwd:
            return func(*args, **kwargs)
        else:
            print("用户名或密码错误。")
    return wrapper


@login                                            ### 利用python的@语法，把decorator置于home函数的定义处 相当于home = login(home)
def home():
    print("欢迎来到XX首页！")

home()
print(home.__name__)                              ### 不使用functools.wraps()时，home的__name__属性变为了wrapper，使用后仍为home
