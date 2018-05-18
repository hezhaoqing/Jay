
#!/usr/bin/env python
# -*- coding: utf_8 -*-

from  conf import *
from threading import Thread
import os
import sys
import time



def threaddo(hostip):						                                                     	 ###### 定义带参数的函数
	ansibledo = "ansible %s -m shell -a \" rm -rf  /opt/hezhaoqing \"     "      % (hostip)
	print(ansibledo)	
	os.system(ansibledo)

	
def main():
    gameserverip = info['host']['gameserver'][userid]                                               ###### 从嵌套字典取ip
    dbserverip   = info['host']['dbserver'][userid]

    th1 = Thread(target=threaddo,args=(gameserverip,))                                              ###### 定义两个线程
    th2 = Thread(target=threaddo,args=(dbserverip,))

    th1.start()
    th2.start()

    th1.join()
    th2.join()


    time.sleep(5)
	
    
if __name__=="__main__":
    userid = sys.argv[1]                                                                          ##### sys 取脚本第一个参数
    main()
	
