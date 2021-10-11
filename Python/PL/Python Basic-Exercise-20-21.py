'''
Python Basic: Exercise-20 with Solution
Write a Python program to get a string which is n (non-negative integer) 
copies of a given string.
'''

def n_copy(input_string, n):
    output = ""
    for i in range(n):
        output = output + input_string        
    return output
    
print(n_copy("AryaVaraste", 8))
print(n_copy("SinaVaraste", 6))


'''
Python Basic: Exercise-21 with Solution
Write a Python program to find whether a given number (accept from the user) 
is even or odd, print out an appropriate message to the user.
'''

number = int(input("Enter a number: "))
if number == 0:
    print("Zero is not even or odd!")
elif (number % 2) == 0:
    print("Entered number is even")
else:
    print("Entered number is odd")