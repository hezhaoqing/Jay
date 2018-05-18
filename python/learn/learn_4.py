#!/usr/bin/env python
# -*- coding: utf_8 -*-

##### 通过命令行传参数，执行某些命令。

from  conf import *
import os
import sys


def main():
        servertype = sys.argv[1]
        userid = sys.argv[2]
        #print servertype 

        ip = info['host'][servertype][userid]

        print "ssh to %s %s %s" % (servertype, userid, ip)

        dossh = "ssh %s" %ip
        #print dossh
        os.system(dossh)

if __name__=="__main__":
        main()
