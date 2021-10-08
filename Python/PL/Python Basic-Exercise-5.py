'''
Python Basic: Exercise-5 with Solution
Write a Python program which accepts the user's first and last name and print 
them in reverse order with a space between them.

input():
In 3.x .raw_input() is renamed to input(). input() function reads a line from 
sys.stdin and returns it with the trailing newline stripped.
To assign the user's name to a variable "y" you can use following command :
y = input('Input your name: ') 
'''

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Hi " + last_name + " " + first_name)

