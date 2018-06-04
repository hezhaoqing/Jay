


*****************************************************************************
* 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的 *
*****************************************************************************



参数组合
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数



1. *args 和 **kw 和 *

*args 称为可变参数，可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
      Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去


**kw  称为关键字参数，关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
      同理在dict前面加两个**号，代表把dict的元素变成关键字参数传进去

    
*     命名关键字参数， 由于关键字参数的函数调用者可以传任意，如果要限制关键字参数的名字，就可以用命名关键字参数，
      和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
      如def person(name, age, *, city, job):
      如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
      如def person(name, age, *args, city, job):
    
如：
def func(a,b,c=2,*d,**e):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

func(1,2,8,1,0,7,name='hzq',age=30)

运行：
1
2
8
(1, 0, 7)
{'name': 'hzq', 'age': 30}





2. argv='xxxx'

以 argv='xxxx' 形式定义的参数  称为默认参数
设置默认参数时，要注意：
    必选参数在前，默认参数在后;
    当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数; 
    默认参数必须指向不变对象！

如：
def enroll(name,gender,age=6,city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

调用方式：                                                ### 调用时，默认参数的位置是对应的，当需要不对应时，要指明默认参数
enroll('Sara','wm')
enroll('alex','m',7)
enroll('juan','wm',city='anyang')
