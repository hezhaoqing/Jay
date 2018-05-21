#!/bin/env python
# -*- coding: utf_8 -*-

### 目的：通过管理机 对所有db服务器执行 数据库备份操作。因为这个操作只针对服务器上的所有数据库进行全备份，而无需区分单台db服务器上的不同用户 不同目录下，
### 使用Python 反而还要对字典中取出的ip进行去重，所以我认为这个Python脚本不如直接对dbserver组执行ansible命令。
### 同样的用法见 learn_3.py、learn_6.py、learn_7.py。像那样需要从同一ip的一台服务器的不同用户的不同目录下进行批量操作 这个脚本就很适合。


from  conf import *
from threading import Thread
import os


#print info['host']['dbserver']['a_mix_02']


def threaddo(hostip):
        ansibledo = "ansible %s -m shell -a \"  cd /data/shellscripts/; bash mysql_backup_one.sh   \" "         % (hostip)
        print ansibledo
        os.system(ansibledo)

def main():
        hostipallrepeat = []                                                      ###### 定义空列表
        for (userid,hostip) in info['host']['dbserver'].items():                  ###### 向空列表中循环追加ip
                hostipallrepeat.append(hostip)
                #print hostipallrepeat

        hostipall = list(set(hostipallrepeat))                                    ###### 把列表转化为元组去重，再转化为列表
        #print hostipall

        for hostip in hostipall:
                #print hostip
                userid = Thread(target=threaddo,args=(hostip,))
                userid.start()

if __name__=="__main__":
        main()
