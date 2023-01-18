import time
from datetime import timedelta, date, datetime
from datetime import time
from datetime import date
import datetime
from datetime import datetime
from sqlite3 import Timestamp
print(datetime.now())

# print(datetime.date.today())

# print(dir(datetime))


# date = datetime.date(2100, 12, 31)
# print(type(date))

print(date(2100, 12, 30))

# Timestamp
# time_stamp = date.fromtimestamp(409999999999999)
# print(time_stamp)

# getting year, month and a day
today = date.today()
print(today.year)
print(today.month)
print(today.day)

# ..............................The time class..............................
time_1 = time()
print('Time A:', time_1)

time_2 = time(13, 55, 00)
print('Time B:', time_2)

time_3 = time(hour=13, minute=55, second=00)
print('Time B:', time_3)

time_4 = time(13, 55, 00, 10000)
print('Time D:', time_4)

time_5 = time(13, 55, 00)
print('hour:', time_5.hour)  # .minute.seconds.microseconds

# ......................The datetime class................
time_1 = datetime(2100, 1, 1)
print(time_1)

time_2 = datetime(2050, 10, 25, 20, 50, 50)
print(time_2)

# getting year, month, etc
time_3 = datetime(2050, 10, 25, 20, 50, 50)
print(time_3.year)
print(time_3.timestamp())

# ...................Timedelta class........................
t1 = date(year=2060, month=12, day=15)
t2 = date(year=2080, month=12, day=15)
print(t2-t1)

t3 = datetime(year=2060, month=12, day=15, hour=12, minute=3)
t4 = datetime(year=2080, month=12, day=15, hour=6, minute=17)
print(t4-t3)

# Diff between two timedelts objects
t5 = timedelta(weeks=2, days=5, hours=1)
t6 = timedelta(weeks=5, days=5, hours=1)
print(t6-t5)

# time duration in seconds
time = timedelta(days=110, hours=24, minutes=110, seconds=10000)
print('total seconds:', time.total_seconds())

# ............................strftime() Method..........................
# formatting using strftime()

now = datetime.now()
# time = now.strftime('%H:%M:%S')
# print(time)
s1 = now.strftime('%m/%d/%Y, %H:%M:%S')
print(s1)

# datetime to str
now = datetime.now()
year = now.strftime('%Y')
month = now.strftime('%m')
day = now.strftime('%d')

# creating string from a timestap
timestamp = 4333336464646422
date_time = datetime.fromtimestamp(timestamp)
print(date_time)
d = date_time.strftime('%m/%d/%y, %H:%M')
print(d)

date2 = date_time.strftime('%d %b, %Y')  # you can capit it
print(date2)

time2 = date_time.strftime('%I%p')  # 03pm
print(time2)

# local's appropriate date and time
timestamp = 2345678923456789
date_time = datetime.fromtimestamp(timestamp)
d1 = date_time.strftime('%c')
print(d1)

# datetime to timestap
now = datetime.now()

# convering to timestap
time_stamp = datetime.timestamp(now)
print(time_stamp)

# converting from timestamp
date_time = datetime.fromtimestamp(time_stamp)
print(date_time)

# ................................Sleep() Method................
print('Immediately')
time.sleep(4.0)
print('Immediately after 4 seconds')
while True:
    local_time = time.localtime()
    result = time.strftime('&I:%M:%S', local_time)
    print(result)
    time.sleep(1)
