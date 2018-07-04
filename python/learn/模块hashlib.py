#!/usr/bin/env python
#coding:utf8

import hashlib

hash1 = hashlib.md5()                  # md5对象，md5不能反解，但是加密是固定的，关系是一一对应，所以有缺陷，可以被对撞出来
hash1.update(bytes('hezhaoqing'))      # 要对哪个字符串进行加密，就放这里
print hash1.hexdigest()                # 加密字符串 04b51c94da8999974dea3c27a03ac36a


hash2 = hashlib.sha384()               # 不同算法，hashlib很多加密算法
hash2.update(bytes('hezhaoqing'))
print(hash2.hexdigest())               # 48c13f7157051079a9bf4da095158403e8984cf8861b50987770d666a37591d70c96c0f7eec6884264027439cf914811


hash3 = hashlib.md5(bytes('jay'))      # 如果没有参数，md5遵守一个规则，生成同一个对应关系，如果加了参数，就在原先加密的基础上再加密一层，这样的话参数只有自己知道，防止被撞库'''
hash3.update(bytes('hezhaoqing'))
print(hash3.hexdigest())               # 8d5549785b1af22397fb91c2c4f1dcc3                        
