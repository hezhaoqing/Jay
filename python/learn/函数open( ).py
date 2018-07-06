#!/usr/bin/env python
# coding:utf-8

f= open('db','r')            ### 只读方式打开文件

print f.read(),              ### 指针在初始位置，返回【字符串形式】f对象，就是整个文件

print f.readline()           ### 读取当前一行，因为刚才有f.read(),当前指针在末尾，所以此处会打印一个空行。

print f.tell()               ### 获得当前指针位置

f.seek(0)                    ### 调指针到开头

print f.readline(),          ### 读取【单行】，此处打印第一行

f.seek(38)                   ### 调指针到第38字符

print f.readline(),          ### 从38字符之后读取一行

print f.readlines(),         ### 读取【剩余所有的行】，返回【列表形式】

print f.name                 ### 返回文本名字

f.close()                    ### 关闭

f= open('db','w+')           ### 写入模式打开文件，相当于 >

f= open('db','a')            ### 追加方式打开文件,相当于 >>

f.write('jay')               ### 在最后一行行尾追加，且不会换行。***注意write只能写入字符串，下面的writelines写入列表
f.write('jay'+'\n')          ### 新的一行追加


f = open('db','w+')
for line in (i**2 for i in range(1,11)):
    f.write(str(line)+'\n')
f.flush()                    ### 把缓冲区内容写入文件，不是很明白，我测试不做flush动作，文件已经写入
f.close()


f = open('db','w+')
listtt = ['j','a','y']
f.writelines(listtt)         ### 把一个列表写入文件，***与上面write的区别。
f.seek(0)
print f.read()               ### 写入结果jay
f.close()


with open("db","a") as f:    ### 为避免打开文件后忘记关闭，通过管理上下文，当【with】代码块执行完毕时，内部会自动关闭并释放文件资源
    f.write('jay')
