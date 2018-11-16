#!/bin/env python
# -*- coding: utf_8 -*-

from  conf import *
from threading import Thread
import os
import sys

#print info['host']['dbserver']['a_mix_02']
 

def threaddo(hostip,userid,logtype):
        ansibledo = "ansible %s -m shell -a \" cat /home/%s/logs/%s | grep 'STARTUP COMPLETED' \"        "      % (hostip, userid, logtype)
        print ansibledo

        os.system(ansibledo)

def main():
        for (userid,hostip) in info['host'][servertype].items():
                #print "userid: " + userid + ", hostip: " + hostip

                userid = Thread(target=threaddo,args=(hostip,userid,logtype))
                userid.start()

if __name__=="__main__": 
        servertype = sys.argv[1]
        logtype = sys.argv[2]
        main()
