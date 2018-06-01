match函数：
尝试用正则表达式模式从字符串的开头匹配，如果匹配成功，返回一个匹配对象;否则返回None
例：
m=re.match('foo','food')      ### 成功匹配
m=re.match('foo','goodfood')  ### 不能匹配


search函数：
在字符串中查找正则表达式模式的第一次出现，如果匹配成功，则返回一个匹配对象;否则返回None
例：
m=re.search('foo','food')      ### 成功匹配
m=re.search('foo','goodfood')  ### 也能匹配


group方法：
使用match或search匹配成功后，返回的匹配对象可以通过group方法获得匹配内容。
例：
re.match('foo','food').group() --- foo
re.search('foo','goodfood').group() --- foo


findall函数：
在字符串中查找正则表达式模式的所有(非重复)出现;返回一个匹配对象的列表。
例：
m=re.findall('foo','goodfood is food') --- ['foo','foo']


finditer函数：
和findall()函数有相同的功能，但返回的不是列表而是迭代器，对于每个匹配，该迭代器返回一个匹配对象.


compile函数：
《1》对正则表达式模式进行编译，返回一个正则表达式对象
《2》不是必须要用这种方式，但是在大量匹配的情况下，可以提升效率


split方法：
《1》根据正则表达式中的分隔符把字符分割为一个列表并返回成功匹配的列表
《2》字符串也有类似的方法， 正则表达式更加灵活。
例：
f='www.baidu.com'
f.split('.')[0] --- www
f.split('.')[1] --- baidu
f.split('.')[2] --- com
f.split('.')[-1] --- com
....


sub方法：
把字符串中所有匹配正则表达式的地方替换成新的字符串
例：
m=re.sub('x','y','axaxax') --- axaxax中的x替换成y



正则匹配：
例： pattern = '\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'          ### 匹配类似于 2018-05-20 13:14:20
    pattern = '[010|021]-\d{8}'                              ### 匹配类似于 010-12345678 或者 021-12345678








