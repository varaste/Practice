'''
Python Basic: Exercise-11 with Solution
Write a Python program to print the documents (syntax, description etc.) of Python 
built-in function(s).
Python Docstring:
A docstring is a string literal that occurs as the first statement in a module, 
function, class, or method definition. Such a docstring becomes the __doc__ special 
attribute of that object.
All modules should normally have docstrings, and all functions and classes exported 
by a module should also have docstrings. 
Public methods (including the __init__ constructor) should also have docstrings.
'''

print(abs.__doc__)
print(sum.__doc__)
print(int.__doc__)


'''
Python Basic: Exercise-12 with Solution
Write a Python program to print the calendar of a given month and year.
Note: Use 'calendar' module.
Python calendar.month(theyear, themonth, w=0, l=0):
The function returns a month’s calendar in a multi-line string using the formatmonth()
of the TextCalendar class.
'l' specifies the number of lines that each week will use.
ex:
      August 2021
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31
'''

import calendar
y = int(input("Enter the year: "))
m = int(input("Enter the month: "))
print(calendar.month(y, m))

'''
Python Basic: Exercise-13 with Solution
Write a Python program to print the following 'here document'.
Sample string:
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
'''

print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")
