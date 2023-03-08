#!/bin/bash

#--------------------------------
# Purpose:     服务器账号统计
# Created:     2023-03-08
#--------------------------------

yum install -y python3

pip3 install openpyxl

cd /tmp

cat >> txt2xlsx.py <<EOF

from openpyxl import Workbook
import os
import sys

f1 = "/tmp/result.xlsx"
wb = Workbook(r'f1')
ws = wb.create_sheet('Sheet1')
shelldo = "cat /etc/passwd | awk -F\: '{print \$1\"-\"\$3\"-\"\$5\"-\"\$6\"-\"\$7}' > users.txt"

os.chdir('/tmp/')
os.system(shelldo)

with open('users.txt', 'r') as f:
        content = f.read().replace('-', '\t')
        lines = content.split('\n')
        for line in lines:
                item = line.split('\t')
                #保存内容
                ws.append(item)
                #print(item)
wb.save(f1)

EOF

python3 txt2xlsx.py
