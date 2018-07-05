#!/usr/bin/env python
# coding:utf-8

f= open('db','r')            ### 只读方式打开文件

print f.read(),              ### 打印f 对象，就是整个文件

print f.readline()           ### 读取当前一行，因为刚才有f.read(),当前指针在末尾，所以此处会打印一个空行。

print f.tell()               ### 获得当前指针位置

f.seek(0)                    ### 调指针到开头

print f.readline(),          ### 此处打印第一行

f.seek(38)                   ### 调指针到第38字符

print f.readline(),          ### 从38字符之后读取一行

print f.readlines(),         ### 读取剩余所有的行，返回一个列表

print f.name                 ### 返回文本名字

f.close()                    ### 关闭




