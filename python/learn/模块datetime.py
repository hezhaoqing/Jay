datetime.datetime.now()                    ###### 获取当前时间。返回结果：2018-05-20 13:14:00.128107
                                                  可以继续.出 年、月、日、时、分、秒、日期、周、时间戳等等。
                        
                        
datetime.datetime.fromtimestamp()          ###### 将时间戳 转化为和上面一样的格式。



datetime.timedelta()                       ###### 设定两个时间之间的间隔，用于时间计算，
                                                  可以设置的单位包括：(days=0, seconds=0, microseconds=0, 
                                                  milliseconds=0, minutes=0, hours=0, weeks=0)，默认都为0。
                                                  
第三个不理解请看下例：
now=datetime.datetime.now()
ago=datetime.timedelta(days=2)
print(now)
print(ago)
print(now-ago)

结果：
2018-05-22 17:59:55.893105
2 days, 0:00:00
2018-05-20 17:59:55.893105
                                                  
                                                  
