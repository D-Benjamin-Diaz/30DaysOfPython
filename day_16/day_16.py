# ====================== Day 16: Python Date Time =============================
"""
Python has a datetime module to handle date and time
"""

import datetime

# There are many functions, but we will focus in a few of them only
print(dir(datetime))
# ['MAXYEAR', 'MINYEAR', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']

# datetime
from datetime import datetime

now = datetime.now()
print(now)  # Prints time RIGHT NOW
day = now.day  # Gets the day as a number (25)
month = now.month  # Gets the month as a number (9)
year = now.year  # Gets the year as a number (2026)
hour = now.hour  # Gets the hour as a number (12)
minute = now.minute  # Gets the minute as number (38)
second = now.second  # Gets the secon as a number (59)

timestamp = now.timestamp()

print(day, month, year, hour, minute)
print("timestamp", timestamp)
print(f"{day}/{month}/{year}, {minute}/{hour}")


# strftime - helps format the date into a string based on the input string code
from datetime import datetime

# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)  # time: 18:21:40
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)  # time one: 06/28/2022, 18:21:40
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)  # time two: 28/06/2022, 18:21:40


# strptime - creates a datetime object based on the string input and a code format
from datetime import datetime

date_string = "5 December, 2019"
print("date_string =", date_string)  # date_string = 5 December, 2019
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)  # date_object = 2019-12-05 00:00:00
