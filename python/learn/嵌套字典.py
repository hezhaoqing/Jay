#!/bin/env python
# -*- coding: utf_8 -*-


info = {
    'host':{
       'gameserver':{
           'i_j_01':'10.10.1.1xx',
           'i_j_02':'10.10.1.1xx',
           'i_j_03':'10.10.1.1xx',
           'i_j_04':'10.10.1.1xx',
           'i_j_05':'10.10.1.1xx',
       },
       'dbserver':{
           'i_j_01':'10.10.5.2xx',
           'i_j_02':'10.10.5.2xx',
           'i_j_03':'10.10.5.2xx',
           'i_j_04':'10.10.5.2xx',
           'i_j_05':'10.10.5.2xx',
       }
    }
}



print(info['host']['gameserver']['i_j_02'])                      ###### 取嵌套字典的某个value : 字典名[key][key][key][key].
	

for (userid,hostip) in info['host']['gameserver'].items():       ###### 用for循环取字典中的键值对 .items()。
    print("userid: " + userid + ", hostip: " + hostip)
