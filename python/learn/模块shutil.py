因为 os.rmdir() 有个毛病，只能删除“空”文件夹。所以只能从最底层的文件夹开始清理，一级一级往上，才能清干净。

后来想想，应该有更简便的方法，因为清空文件夹是很常见的动作。查了Python官方文档，发现了os以外的另一个模块：shutil（高级文件操作），

竟然有 shutil.rmtree() 的方法，不仅是清空，直接连文件夹都一起删掉，太凶残了！

shutil.rmtree('/opt/hzq') 等同于 rm -fr /opt/hzq

为了“仅仅清空”，我搭配使用 shutil 模块重写了代码：


#!/usr/bin/env python

import shutil,os

os.chdir('/opt/hzq') #进入要清空的目录
ds = list(os.listdir('.')) #获得该目录下所有文件或文件夹列表
for d in ds: #遍历该列表
    if os.path.isfile(d): #如果列表项是文件
        os.remove(d) #直接删除
    else: #如果不是文件，肯定是文件夹
        shutil.rmtree(d) #也直接删除
