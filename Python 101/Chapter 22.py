import datetime as dt
import time
print(time.gmtime(0))
"""
d = dt.date(2012,12,14)
d_t = dt.datetime(2014,3,5)
dtn = dt.datetime.today()
print(d)
print(dt)
print(dtn)

#f_time = dt.datetime.today().strftime("%Y%m%d")
#print(f_time)

today = dt.datetime.today()
print(today.strftime("%m/%d/%Y"))

print(today.strftime("%Y-%m-%d-%H.%M.%S"))

dt_future = dt.datetime(2034,2,26)
delta = dt_future-today
print(delta.days)
print(delta.total_seconds())
"""
print(time.ctime())
print(time.ctime(13841126390))

"""
for x in range(5):
    time.sleep(2)
    print("Slept for 2 seconds")
"""

print(time.time())