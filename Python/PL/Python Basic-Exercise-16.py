'''
Python Basic: Exercise-16 with Solution
Write a Python program to get the difference between a given number and 17, if 
the number is greater than 17 return double the absolute difference.
'''

number = int(input("Enter your number: "))
def e16(number):
    if number > 17:
        return 2 * (number - 17)
    else:
        return 17 - number
    
print(e16(number))