# 1. Date - Time module in python

# Get current date and time
# create custome dates
# format dates
# perform data calculation

# Importing datetime Module

import datetime

now = datetime.datetime.now

print(now)

# current Date only

today = datetime.date.today()

print(today)

# custom date

custom = datetime.date(2024,12,24)

print(custom)

# Access year , month , day

today = datetime.date.today()

print("Year :",today.year)
print("Month :",today.month)
print("Day :",today.day)

# strftime() is used to format date and time

now = datetime.datetime.now()

formatted = now.strftime("%d-%m-%y %H:%M:%S")

print(formatted)

# date difference

d1 = datetime.date(2009,1,1)
d2 = datetime.date(2026,6,11)

difference = d2 - d1

print(difference.days)

# 2. time module in Python

# working with system time

# Dealys in program

# Mesuring execution time

# Import time module

import time

current = time.time()

print(current)

# It returns seconds from Tanuary 1 , 1970

# pause program using sleep()

print("start")

time.sleep(3)

print("End after 3 seconds")

# current localtime

local = time.localtime()

print(local)

# format time

current = time.strftime("%H:%M:%S")

print(current)

# measure Execution time

start = time.time()

for i in range(1000000):
    pass

end = time.time()

print("Execution time:",end-start)

# 1. Display Current Date and Time

from datetime import datetime

now = datetime.now()

print(now)
print("Year:",now.year)
print("Month:",now.month)
print("Day:",now.day)
print("Hour:",now.hour)
print("Minute:",now.minute)
print("Second:",now.second)

# 1. datetime.date.today()
# return current date and time

# 2. datetime.date.today()
# return current date

# 3. datetime.datetime.today()
# return current local date and time

# 4. datetime.datetime.utcnow
# return current utctime.

import datetime

print(datetime.datetime.utcnow())

# 5. strftime()
# format date/time into string

# 6. strotime()
# convert string into datetime object.

from datetime import datetime

date = "2025-06-11"

obj = datetime.strptime(date,"%Y-%M-%D")

print(obj)

# 7. timedelta

# used to date calculation

from datetime import datetime, time delta

today = datetime.now()
future = today+timedelta(days = 5)

print(future)

# 8. replace()

# replaces year/month/day etc.....

now = date.time.now()

new_date = now.replace(year=2030)

print(new_date)

# 9. date()
# Extract only date.

# 10. time()
# Extract only time.

# 11. Weekdays()
# return weekday number.

now = datetime.now()

print(now.weekday())

# 12. isoweekday()
# return readable weekdays
number(1-7)

now = datetime.now()

print(now.iosweekday())

# 13. ctime
# return readable date and time

now =datetime.now()

print(now.ctime)

# 14. timestamp()
# return second since epoch.

now = datetime.now()

print(now.timestamp())

# 15. fromtimestamp()
# converts timestamp to datetime.

s= 1749863000

print(datetime.fromtimestemp(s))

# python time module method

# 1. time()
# 2. ctime()
# 3. sleep()
# 4. localtime()
# 5. gmtime()
# return UTC time object.

importtime

print(time.gmtime())

# 6. strftime()
# 7. strptime()
# 8. mktime()
# converts time tuple in seconds

import time

t = time.localtime()

print(time.mktime(t))

# 9. asctime()

import time

t=time.localtime()

print(time.asctime(t))

# 10. perf_counter()
# 11. proccess_time()
# 12. monotomic()
# returns continuesly increasing clock value.

import time

print(time.monotonic)



























































































































































































































