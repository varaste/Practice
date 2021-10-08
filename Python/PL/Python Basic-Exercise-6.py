'''
Python Basic: Exercise-6 with Solution
Write a Python program which accepts a sequence of comma-separated numbers 
from user and generate a list and a tuple with those numbers.

Python list:
A list is a container which holds comma separated values (items or elements) 
between square brackets where items or elements need not all have the same type. 
In general, we can define a list as an object that contains multiple data items 
(elements). The contents of a list can be changed during program execution. 
The size of a list can also change during execution, as elements are added or 
removed from it.
Python tuple:
A tuple is container which holds a series of comma separated values 
(items or elements) between parentheses such as an (x, y) co-ordinate. 
Tuples are like lists, except they are immutable (i.e. you cannot change its 
content once created) and can hold mix data types.
'''

vals = input("Enter values comma seprated: ")
v_list = vals.split(",")
v_tuple = tuple(v_list)
print("List: ", v_list)
print("Tuple ", v_tuple)