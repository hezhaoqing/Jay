常用函数:
fileinput.input()       #返回能够用于for循环遍历的对象              ### 下面的函数基于此函数，此函数要输入文件。
fileinput.filename()    #返回当前文件的名称
fileinput.lineno()      #返回当前已经读取的行的数量（或者序号）       ### 用于批量读入文件时，记录行
fileinput.filelineno()  #返回当前读取的行的行号
fileinput.isfirstline() #检查当前行是否是文件的第一行
fileinput.isstdin()     #判断最后一行是否从stdin中读取
fileinput.close()       #关闭队列

关键函数：
fileinput.input(files='filename', inplace=False, backup='', bufsize=0, mode='r', openhook=None)
files:         #文件的路径列表，默认是stdin方式，多文件['1.txt','2.txt',...]
inplace:       #是否将标准输出的结果写回文件，默认不取代.  可以用True False   也可以用 1 0.
backup:        #备份文件的扩展名，只指定扩展名，如.bak。如果该文件的备份文件已存在，则会自动覆盖。
bufsize:       #缓冲区大小，默认为0，如果文件很大，可以修改此参数，一般默认即可
mode:　　　　　　#读写模式，默认为只读，FileInput opening mode must be one of 'r', 'rU', 'U' and 'rb'
openhook:　　　 #该钩子用于控制打开的所有文件，比如说编码方式等;


一。修改文件并备份源文件：
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import fileinput
for i in fileinput.input('/data/shellscripts/test.txt',inplace=True,backup='.back'):   ### 遍历每行，输出覆盖原文，并把原文件备份为.back
        i=i.replace('123456','xxx')                                                    ### 匹配到123456的行，123456替换为xxx
        print i,                                                                       ### 不加逗号，会每次打印1个空行，加上逗号即可。

二。打印行号及内容
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import fileinput
for i in fileinput.input('test.txt'):
	i_n=fileinput.lineno()
	print i_n,l,

三。见 learn_010.py
