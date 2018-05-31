#!/usr/bin/env python
# -*- coding: utf_8 -*-

from  conf import *
from threading import Thread
import os
import sys
import time


def threaddo(hostip):                                                                               ###### 定义带参数的函数
	ansibledo = "ansible %s -m shell -a \" rm -rf  /opt/hezhaoqing \"     "      % (hostip)
	print(ansibledo)                                                                                ###### 打印 不是必要的。
	os.system(ansibledo)                                                                            ###### 把打印的命令交给命令行执行

	
def main():
    gameserverip = info['host']['gameserver'][userid]                                               ###### 从嵌套字典取ip
    dbserverip   = info['host']['dbserver'][userid]

    th1 = Thread(target=threaddo,args=(gameserverip,))                                              ###### 定义两个线程
    th2 = Thread(target=threaddo,args=(dbserverip,))

    th1.start()											                                            ###### 开始线程
    th2.start()

    th1.join()                                                                                      ###### 阻塞下面的进程 直到上面结束再调用
    th2.join()	
    
    ansibledo1 = "ansible %s -m shell -a \" su - %s -c ' cd /home/%s/; bash do.sh allb ' \"     "     % (dbserverip, userid, userid)
    print(ansibledo1)
    os.system(ansibledo1)

    time.sleep(5)

    ansibledo2 = "ansible %s -m shell -a \" su - %s -c ' cd /home/%s/; bash do.sh alla  ' \"     "    % (gameserverip, userid, userid)
    print(ansibledo2)
    os.system(ansibledo2)
	
    
if __name__=="__main__":
    userid = sys.argv[1]                                                                            ###### sys 取脚本第一个参数
    main()
	
