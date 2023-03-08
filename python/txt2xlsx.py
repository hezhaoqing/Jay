#导入openpyxl用于excel操作
from openpyxl import Workbook
import os
import sys
### shell
shell1 = "cat /etc/passwd | awk -F\: '{print $1\"-\"$3\"-\"$5\"-\"$6\"-\"$7}' > /root/users.txt"
#print(shell1)

#新建保存结果的excel，sheet
wb = Workbook(r'result.xlsx')
ws = wb.create_sheet('Sheet1')


os.system(shell1)
#打开txt文件，把-替换成统一的\t
with open('users.txt', 'r') as f:
        content = f.read().replace('-', '\t')
        lines = content.split('\n')
        for line in lines:
                item = line.split('\t')
                #保存内容
                ws.append(item)
                #print(item)
#保存excel文件
wb.save('result.xlsx')
