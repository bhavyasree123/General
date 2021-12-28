import time
x = time.time() #gives the current time in seconds
print(x)
y = time.ctime()
print(y) #gives the current time like this Tue Dec 28 13:40:19 2021
z = time.localtime()#time.struct_time(tm_year=2021, tm_mon=12, tm_mday=28, tm_hour=13, tm_min=41, tm_sec=35, tm_wday=1, tm_yday=362, tm_isdst=0)
print(z)