#!/usr/bin/env python
# -*- coding: utf_8 -*-

import os
import platform
import time
import random
from file import *                                  		       	 ###### 从某文件导入。比如在某个文件定义一些字典。
from threading import Thread                    		  	 ###### 线程. 从模块导入类。用法见learn_2.py
import sys




DIR = "/opt/hezhaoqing"                

def main():								 ###### 定义一个没有参数的函数
	if not os.path.exists(DIR)
		os.mkdir(DIR)

	print(platform.system())                        	         ###### Linux

	print(time.strftime("%Y-%m-%d %H:%M:%S"))	                 ###### 2018-05-20 20:13:14
	time.sleep(1)							 ###### 休眠1秒
	
	print(info['host']['gameserver']['userid'])                      ###### 取嵌套字典的某个value : 字典名[key][key][key][key].
	
	print(myargv)

	for (userid,hostip) in info['host']['gameserver'].items():       ###### 用for循环取字典中的键值对 .items()。
		print("userid: " + userid + ", hostip: " + hostip)
	
	

if __name__ == "__main__":                                               ###### 被调用不执行，被直接执行才执行。

	myargv= sys.argv[1]						 ###### 定义上面要打印的myargv 为脚本的第一个参数
	
	main()
