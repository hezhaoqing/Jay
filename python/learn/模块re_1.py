Python 的re模块提供了对正则表达式的支持。主要用到的方法列举如下：
#返回pattern对象
re.compile(string[,flag])  
#以下为匹配所用函数
re.match(pattern, string[, flags])
re.search(pattern, string[, flags])
re.split(pattern, string[, maxsplit])
re.findall(pattern, string[, flags])
re.finditer(pattern, string[, flags])
re.sub(pattern, repl, string[, count])
re.subn(pattern, repl, string[, count])




（一）re.match(pattern, string[, flags])
从string（我们要匹配的字符串）的开头开始，尝试匹配pattern，一直向后匹配，
如果遇到无法匹配的字符，立即返回None，
如果匹配未结束已经到达string的末尾，也会返回None。
两个结果均表示匹配失败，否则匹配pattern成功，同时匹配终止，不再对string向后匹配
# -*- coding: utf-8 -*- 
#导入re模块
import re 
# 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
pattern = re.compile(r'hello') 
# 使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
result1 = re.match(pattern,'hello')
result2 = re.match(pattern,'helloo Q!')
result3 = re.match(pattern,'helo Q!')
result4 = re.match(pattern,'hahahello Q!') 
#如果1匹配成功
if result1:
    # 使用Match获得分组信息
    print result1.group()
else:
    print '1匹配失败！' 
#如果2匹配成功
if result2:
    # 使用Match获得分组信息
    print result2.group()
else:
    print '2匹配失败！' 
#如果3匹配成功
if result3:
    # 使用Match获得分组信息
    print result3.group()
else:
    print '3匹配失败！' 
#如果4匹配成功
if result4:
    # 使用Match获得分组信息
    print result4.group()
else:
    print '4匹配失败！'
    
    
    
    
（二）re.search(pattern, string[, flags]) 
search方法与match方法极其类似，
区别在于match()函数只检测re是不是在string的开始位置匹配，
search()会扫描整个string查找匹配，
match（）只有在0位置匹配成功的话才有返回，如果不是开始位置匹配成功的话，match()就返回None。
同样，search方法的返回对象同样有match()返回对象的方法和属性




（三）re.split(pattern, string[, maxsplit])
按照能够匹配的子串将string分割后返回列表。maxsplit用于指定最大分割次数，不指定将全部分割。
import re 
pattern = re.compile(r'\d+')
print re.split(pattern,'one1two222three33four4five')




（四）re.findall(pattern, string[, flags])
以列表形式返回全部能匹配的子串
import re 
pattern = re.compile(r'\d+')
print re.findall(pattern,'one1two2three3four4')




（五）re.finditer(pattern, string[, flags])
返回一个顺序访问每一个匹配结果（Match对象）的迭代器
import re 
pattern = re.compile(r'\d+')
for m in re.finditer(pattern,'one1two2three3four4'):
    print m.group(),


    
 
（六）re.sub(pattern, repl, string[, count])
使用repl替换string中每一个匹配的子串后返回替换后的字符串。
当repl是一个字符串时，可以使用\id或\g、\g引用分组，但不能使用编号0。
当repl是一个方法时，这个方法应当只接受一个参数（Match对象），并返回一个字符串用于替换（返回的字符串中不能再引用分组）。
count用于指定最多替换次数，不指定时全部替换。    
import re
pattern = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!' 
print re.sub(pattern,r'\2 \1', s)
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
print re.sub(pattern,func, s)
### output ###
# say i, world hello!
# I Say, Hello World!    
    
    
    
    
（七）re.subn(pattern, repl, string[, count])    
 返回 (sub(repl, string[, count]), 替换次数)。   
    
    




*** Python Re模块的另一种使用方式 ***
在上面7个方法的调用方式都是 re.match，re.search的方式，
其实还有另外一种调用方式，可以通过pattern.match，pattern.search调用，
这样调用便不用将pattern作为第一个参数传入了，想怎样调用皆可。
***
