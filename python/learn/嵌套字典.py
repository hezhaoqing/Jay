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



for user,ip in info['host']['gameserver'].items()      ### 取字典gameserver中的所有元素

