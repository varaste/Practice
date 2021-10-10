'''
Python Basic: Exercise-17 with Solution
Write a Python program to test whether a number is within 100 of 1000 or 2000.
Python abs(x) function:
The function returns the absolute value of a number. 
The argument may be an integer or a floating point number. 
If the argument is a complex number, its magnitude is returned.
'''

def near_thousand(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))   
print(near_thousand(2200))


'''
Python Basic: Exercise-18 with Solution
Write a Python program to calculate the sum of three given numbers, 
if the values are equal then return thrice of their sum.
'''

def sum3(x, y, z):
    if x == y == z:
        return 3 * (x + y + z)
    else:
        return x + y + z
    
print(sum3(5, 2, 8))
print(sum3(8, 8, 8))


'''
Python Basic: Exercise-19 with Solution
Write a Python program to get a new string from a given string where "Is" 
has been added to the front. 
If the given string already begins with "Is" then return the string unchanged.
'''

def str_is(my_string):
    if len(my_string) >= 2 and my_string[:2] == "Is":
        return my_string
    else:
        return "Is" + my_string

print(str_is("Array"))
print(str_is("IsEmpty"))