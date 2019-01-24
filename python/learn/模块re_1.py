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
