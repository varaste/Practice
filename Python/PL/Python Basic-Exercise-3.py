'''
Write a Python program to display the current date and time.

Python datetime:

The datetime module supplies classes for manipulating dates and times in both 
simple and complex ways.
datetime.now(tz=None) returns the current local date and time. 
If optional argument tz is None or not specified, this is like today().
date.strftime(format) returns a string representing the date, 
controlled by an explicit format string. 
Format codes referring to hours, minutes or seconds will see 0 values.
'''

import datetime

now = datetime.datetime.now()
print("Current date and time: ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))


