#!/usr/bin/env python
# -*- coding: utf_8 -*-

import os
import platform
import time
import random
from file import *                                        ###### 从某文件导入。比如在某个文件定义一些字典。
from threading import Thread                              ###### 线程. 从模块导入类。

DIR = "/opt/hezhaoqing"                

def main():
	if not os.path.exists(DIR)
		os.mkdir(DIR)

	print(platform.system())                              ###### Linux

	print(time.strftime("%Y-%m-%d %H:%M:%S"))	          ###### 2018-05-20 20:13:14

	gameserverip = info['host']['gameserver'][userid]     ###### 取嵌套字典的某个value
	
	
	

if __name__ == "__main__":                                ###### 被调用不执行，被直接执行才执行。
	main()