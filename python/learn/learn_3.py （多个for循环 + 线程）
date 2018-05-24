#!/usr/bin/env python
# -*- coding: utf_8 -*-

#### 用多个for循环 多个线程 让不同类型的服务器  并行执行 任务

from  conf import *
from threading import Thread
import os

#print info['host']['dbserver']['a_mix_02']


def threaddo(hostip,userid,servertype):
        import time
        currenttime = time.strftime("%Y%m%d",time.localtime(time.time()))
        #currenttime = "20160817"
        ansibledo = "ansible %s -m shell -a \"du -sh  /home/%s/backup/* | grep %s \"     "      % (hostip, userid, currenttime)
        print ansibledo

        os.system(ansibledo)

def main():
        for (userid,hostip) in info['host']['gameserver'].items():
                #print "userid: " + userid + ", hostip: " + hostip

                userid = Thread(target=threaddo,args=(hostip,userid,'gameserver'))
                userid.start()

        for (userid,hostip) in info['host']['dbserver'].items():
                #print "userid: " + userid + ", hostip: " + hostip

                userid = Thread(target=threaddo,args=(hostip,userid,'dbserver'))
                userid.start()

        for (userid,hostip) in info['host']['combatserver'].items():
                #print "userid: " + userid + ", hostip: " + hostip

                userid = Thread(target=threaddo,args=(hostip,userid,'combatserver'))
                userid.start()

        for (userid,hostip) in info['host']['worldserver'].items():
                #print "userid: " + userid + ", hostip: " + hostip

                userid = Thread(target=threaddo,args=(hostip,userid,'worldserver'))
                userid.start()

if __name__=="__main__":
        main()
