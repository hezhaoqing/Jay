#!/bin/env python
# -*- coding: utf_8 -*-

### 通过管理机 对所有db服务器执行 数据库备份操作。


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
